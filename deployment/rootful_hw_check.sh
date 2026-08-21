#!/usr/bin/env bash
set -euo pipefail

# Rootful hardware validation for Trilobot compose service.
# Usage:
#   ./deployment/rootful_hw_check.sh [path/to/deployment/compose.yml]

ROOTFUL_HOST="unix:///var/run/docker.sock"
SERVICE_NAME="trilobot-driver"
CONTAINER_NAME="trilobot_hardware_bridge"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

COMPOSE_FILE="${1:-${REPO_ROOT}/deployment/compose.yml}"
if [[ ! -f "${COMPOSE_FILE}" ]]; then
  echo "ERROR: compose file not found: ${COMPOSE_FILE}" >&2
  echo "Try: ./deployment/rootful_hw_check.sh /absolute/path/to/deployment/compose.yml" >&2
  exit 1
fi

if ! command -v docker >/dev/null 2>&1; then
  echo "ERROR: docker is not installed or not on PATH" >&2
  exit 1
fi

if ! command -v sudo >/dev/null 2>&1; then
  echo "ERROR: sudo is required for rootful daemon checks" >&2
  exit 1
fi

if sudo -n true 2>/dev/null; then
  SUDO="sudo -n"
else
  SUDO="sudo"
fi

echo "=== 0) Inputs ==="
echo "Compose file: ${COMPOSE_FILE}"
echo "Service: ${SERVICE_NAME}"
echo "Rootful host: ${ROOTFUL_HOST}"
echo

echo "=== 1) Daemon mode check ==="
echo "Current user context: $(docker context show 2>/dev/null || echo unknown)"
docker info 2>/dev/null | grep -E "Context:|rootless|userns|Security Options" || true
echo
echo "Rootful context check:"
$SUDO docker --host "${ROOTFUL_HOST}" info 2>/dev/null | grep -E "Context:|rootless|userns|Security Options" || true
echo

echo "=== 2) Clear rootful container-name conflict (if present) ==="
$SUDO docker --host "${ROOTFUL_HOST}" ps -a --filter "name=^/${CONTAINER_NAME}$" || true
if $SUDO docker --host "${ROOTFUL_HOST}" ps -a --format '{{.Names}}' | grep -qx "${CONTAINER_NAME}"; then
  echo "Removing existing rootful container: ${CONTAINER_NAME}"
  $SUDO docker --host "${ROOTFUL_HOST}" rm -f "${CONTAINER_NAME}" >/dev/null
fi
echo

echo "=== 3) Start hardware bridge in rootful daemon ==="
$SUDO docker --host "${ROOTFUL_HOST}" compose -f "${COMPOSE_FILE}" up -d "${SERVICE_NAME}"
echo

echo "=== 4) Resolve container id ==="
CID="$($SUDO docker --host "${ROOTFUL_HOST}" compose -f "${COMPOSE_FILE}" ps -q "${SERVICE_NAME}")"
if [[ -z "${CID}" ]]; then
  echo "ERROR: could not resolve container id for service ${SERVICE_NAME}" >&2
  exit 1
fi
echo "CID=${CID}"
echo

echo "=== 5) HostConfig sanity ==="
$SUDO docker --host "${ROOTFUL_HOST}" inspect "${CID}" --format '
Name={{.Name}}
Privileged={{.HostConfig.Privileged}}
UsernsMode={{.HostConfig.UsernsMode}}
User={{.Config.User}}
Devices={{json .HostConfig.Devices}}
CapAdd={{json .HostConfig.CapAdd}}
SecurityOpt={{json .HostConfig.SecurityOpt}}
'
echo

echo "=== 6) In-container GPIO/I2C checks ==="
PROBE_SCRIPT='set +e
echo "id: $(id)"
ls -l /dev/gpiochip0 /dev/gpiochip4 /dev/i2c-1 2>/dev/null || true

if command -v i2cdetect >/dev/null 2>&1; then
  echo "--- i2cdetect -y 1 ---"
  i2cdetect -y 1 || true
else
  echo "i2cdetect not available in container"
fi

echo "--- Python GPIO/I2C probe ---"
python3 - <<PY
import sys
import traceback
print("python:", sys.version)

try:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    print("GPIO open: OK")
except Exception as e:
    print("GPIO open: FAIL ->", repr(e))
    traceback.print_exc()

try:
    from smbus2 import SMBus
    bus = SMBus(1)
    bus.close()
    print("SMBus(1): OK")
except Exception as e:
    print("SMBus(1): FAIL ->", repr(e))
    traceback.print_exc()
PY'

if ! $SUDO docker --host "${ROOTFUL_HOST}" exec "${CID}" sh -lc "${PROBE_SCRIPT}"; then
  echo
  echo "Container is not stable enough for exec; running fallback one-off probe container."
  echo "This uses the same service config but overrides the command for diagnostics."
  $SUDO docker --host "${ROOTFUL_HOST}" compose -f "${COMPOSE_FILE}" run --rm --no-deps --entrypoint sh "${SERVICE_NAME}" -lc "${PROBE_SCRIPT}"
fi
echo

echo "=== 7) Recent service logs ==="
$SUDO docker --host "${ROOTFUL_HOST}" logs --tail 120 "${CID}" || true
echo

echo "=== 8) Result hint ==="
echo "If rootful checks pass here but rootless mode fails, keep this service on rootful docker."
