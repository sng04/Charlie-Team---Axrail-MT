#!/bin/bash
# Build the Strands Agents Lambda layer for Python 3.11
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="$SCRIPT_DIR/python"

echo "Cleaning previous build..."
rm -rf "$TARGET_DIR"

echo "Installing strands-agents and strands-agents-builder..."
pip3 install \
    strands-agents \
    strands-agents-builder \
    -t "$TARGET_DIR" \
    --platform manylinux2014_x86_64 \
    --only-binary=:all: \
    --python-version 3.11 \
    --no-cache-dir

echo "Layer build complete: $TARGET_DIR"
