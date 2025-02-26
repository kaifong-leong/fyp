# Use the OpenQuantumSafe OpenSSL 3 image as the base
FROM openquantumsafe/ci-ubuntu-jammy:latest AS builder

# Create a non-root user
RUN useradd -m -s /bin/bash testssl

# Install dependencies
RUN apt-get update && \
    apt-get install -y git bash util-linux bsdmainutils dnsutils bind9-host && \
    rm -rf /var/lib/apt/lists/*

# Clone the testssl.sh repository
RUN git clone https://github.com/testssl/testssl.sh.git /opt/testssl.sh

# Set the working directory
WORKDIR /opt/testssl.sh

# Make testssl.sh executable
RUN chmod +x testssl.sh

# Clean unnecessary files to reduce image size
RUN rm -rf /var/lib/apt/lists/* \
    /usr/share/doc \
    /usr/share/man \
    /usr/share/locale

# Set up a directory inside the container for output files
RUN mkdir -p /opt/testssl.sh/results && \
    chown -R testssl:testssl /opt/testssl.sh

# Copy the entrypoint script into the container
COPY entrypoint.sh /opt/testssl.sh/entrypoint.sh
RUN chmod +x /opt/testssl.sh/entrypoint.sh

# Switch to non-root user
USER testssl

# Use the custom script as the entry point
ENTRYPOINT ["bash", "/opt/testssl.sh/entrypoint.sh"]

# # Set the entrypoint to testssl.sh
# ENTRYPOINT ["bash", "./testssl.sh"]
# CMD ["-h"]