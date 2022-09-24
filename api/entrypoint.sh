#!/bin/bash

echo "Image Versions:"
echo "   pip3    : `pip3 -V | cut -d ' ' -f 2`"
echo "   python3 : `python3 -V | cut -d ' ' -f 2`"

# Install packages
pip3 --disable-pip-version-check install --root-user-action=ignore -r requirements.txt | grep -v 'already satisfied'

# Run whatever command was passed on
exec "$@"