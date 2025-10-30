#!/usr/bin/env bash
set -euo pipefail

python3 -m venv venv
# shellcheck disable=SC1091
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
echo "Environment ready."
