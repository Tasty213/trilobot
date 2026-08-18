# Use the official Python image matching the current Raspberry Pi OS (Bookworm)
FROM python:3.11-slim-bookworm

# Install system dependencies often needed for Pi development (GPIO, I2C, Build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    python3-dev \
    libgpiod-dev \
    i2c-tools

ADD trilobot-python trilobot-python
RUN pip install ./trilobot-python
