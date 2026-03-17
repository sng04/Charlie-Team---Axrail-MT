#!/bin/bash
set -e
cd "$(dirname "$0")"
rm -rf python
pip3 install -r requirements.txt -t python/ --quiet
echo "PyPDF2 layer built successfully."
