#!/bin/sh
set -x
# Variable precedence is environment variable defined, then command line supplied,
# and finally default values.
SERVER_IP="${SERVER_IP:-${1:-127.0.0.1}}"
PASSPHRASE="${PASSPHRASE:-${2:-Password1}}"
python server.py $SERVER_IP $PASSPHRASE
