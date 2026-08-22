#!/bin/bash
set -e

# Source ROS and colcon setup files
source /opt/ros/lyrical/setup.bash
source /workspace/install/setup.bash

# Execute the command passed to the container
exec "$@"
