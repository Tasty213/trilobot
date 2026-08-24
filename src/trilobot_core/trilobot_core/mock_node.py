from unittest.mock import MagicMock

import rclpy
from rclpy.executors import ExternalShutdownException
from trilobot import Trilobot

from trilobot_core.drivers.driver_service import DriverService


def main():
    try:
        with rclpy.init():
            mock_trilobot = MagicMock(Trilobot)
            driver_service = DriverService(mock_trilobot)

            rclpy.spin(driver_service)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == "__main__":
    main()
