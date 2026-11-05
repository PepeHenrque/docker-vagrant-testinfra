FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --break-system-packages ansible-core pytest pytest-testinfra
