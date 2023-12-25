#!/bin/sh
set -x
SERVER_IP="${SERVER_IP:-127.0.0.1}"
PASSPHRASE="${PASSPHRASE:-Password1}"
python server.py $SERVER_IP $PASSPHRASE
