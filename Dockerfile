# Build stage
FROM ros:lyrical-ros-core AS builder

# install ros package
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-demo-nodes-cpp \
    ros-${ROS_DISTRO}-demo-nodes-py && \
    rm -rf /var/lib/apt/lists/*

# Install system dependencies often needed for Pi development (GPIO, I2C, Build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    python3-dev \
    pip \
    libgpiod-dev \
    i2c-tools \
    ssh \
    sudo \
    software-properties-common

RUN apt install python3-colcon-common-extensions python3-rosdep --yes
RUN rosdep init
RUN rosdep update

WORKDIR /workspace

COPY . .

RUN colcon build --packages-select trilobot_core

# Runtime stage
FROM ros:lyrical-ros-core

# Install only runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-colcon-common-extensions \
    python3-rosdep && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

# Copy only the install directory from builder
COPY --from=builder /workspace/install /workspace/install

COPY entrypoint.sh /workspace/entrypoint.sh
RUN chmod +x /workspace/entrypoint.sh

ENTRYPOINT ["/workspace/entrypoint.sh"]
CMD ["ros2", "run", "trilobot_core", "driver_node"]
