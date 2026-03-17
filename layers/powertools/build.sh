#!/bin/bash
set -e
cd "$(dirname "$0")"
rm -rf python
pip3 install -r requirements.txt -t python/ \
    --platform manylinux2014_x86_64 \
    --only-binary=:all: \
    --python-version 3.11 \
    --quiet
echo "Powertools layer built successfully."
