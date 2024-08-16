#!/bin/sh

INITIAL_FILE1="/var/app/initial"
INITIAL_FILE2="/tmp/initial" # For case recreate container

if [ ! -e "$INITIAL_FILE1" ] || [ ! -e "$INITIAL_FILE2" ]; then
    echo "Installing packages...."
    # rm -rf /var/app/.venv
    # rm -rf /var/app/.cache
    # python -m venv .venv
    # source .venv/bin/activate
    pip install -r requirements.txt
    touch $INITIAL_FILE1
    touch $INITIAL_FILE2
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] Remove this file and restart the container to reinstall packages" > $INITIAL_FILE1
    echo "Finished install packages...."
fi

tail -f /dev/null