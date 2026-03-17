#!/bin/bash
set -e

# Build the OpenSearch Lambda layer
# Installs dependencies into python/ directory for Lambda layer packaging

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

cd "$SCRIPT_DIR"

# Clean previous build
rm -rf python/

# Install dependencies into python/ directory
pip3 install -r requirements.txt -t python/

echo "OpenSearch layer built successfully in ${SCRIPT_DIR}/python/"
