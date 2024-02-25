# Filename: server.py
# Created By: Mackenly Jones on 07/12/2022
# Web: mackenly.com
# Twitter: @mackenlyjones

import os
import argparse
import logging
import json
import PyATEMMax
from api.Api import Api
from http.server import *

# create the switcher object
switcher = PyATEMMax.ATEMMax()
api = Api(switcher)
passphrase = ''
ip = ''


class GFG(BaseHTTPRequestHandler):
    # on GET...
    def do_GET(self):
        global passphrase, ip
        if self.headers.get('Authorization') == passphrase:
            # http response code - success
            self.send_response(200)
            # http header - content type - html
            self.send_header('Content-type', 'application/json')
            # CORS headers
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Authorization')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            # http body - json
            self.wfile.write(bytes(str(json.dumps(api.get(self.path, passphrase, ip))), "utf8"))
            log.info("GET request received, sent response")
        else:
            # http response code - unauthorized
            self.send_response(401)
            # http header - content type - html
            self.send_header('Content-type', 'application/json')
            # CORS headers
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Authorization')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            # http body - json
            self.wfile.write(b'{"error": "unauthorized"}')
            log.error("GET request received, unauthorized")
        return

    # on POST...
    def do_POST(self):
        global passphrase, ip
        if self.headers.get('Authorization') == passphrase:
            # http response code - success
            self.send_response(200)
            # http header - content type - html
            self.send_header('Content-type', 'application/json')
            # CORS headers
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Authorization')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            # http body - json
            self.wfile.write(bytes(str(json.dumps(api.post(self.path, passphrase, ip))), "utf8"))
            log.info("POST request received, sent response")
        else:
            # http response code - unauthorized
            self.send_response(401)
            # http header - content type - html
            self.send_header('Content-type', 'application/json')
            # CORS headers
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Authorization')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            self.end_headers()
            # http body - json
            self.wfile.write(b'{"error": "unauthorized"}')
            log.error("POST request received, unauthorized")
        return

    # on OPTIONS...
    def do_OPTIONS(self):
        global passphrase, ip
        # http response code - success
        self.send_response(200)
        # http header - content type - html
        self.send_header('Content-type', 'application/json')
        # CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Authorization')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        # http body - json
        self.wfile.write(bytes(str(json.dumps(api.options(self.path, passphrase, ip))), "utf8"))
        log.info("OPTIONS request received, sent response")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', help='switcher IP address')
    parser.add_argument('--passphrase', help='passphrase to compare requests to', type=str, default='Password1')
    args = parser.parse_args()

    # set global variables
    global passphrase, ip
    passphrase = os.environ.get('PASSPHRASE', args.passphrase)
    ip = os.environ.get('SERVER_IP', args.ip)

    # if no ip is provided, exit
    if ip is None:
        log.error("No IP address provided")
        exit()

    log.info("Initializing switcher")
    switcher.setLogLevel(logging.INFO) # Set switcher verbosity (try DEBUG to see more)
    switcher.connect(ip)

    log.info("Waiting for connection")
    switcher.waitForConnection()

    log.info("Connected to switcher")

    # this is the object which take port
    # number and the server-name
    # for running the server
    port = ThreadingHTTPServer(('', 5555), GFG)

    # this is used for running our
    # server as long as we wish
    # i.e. forever
    log.info("Starting API server on http://localhost:" + str(port.server_port))
    port.serve_forever()


# setup logging
logging.basicConfig( datefmt='%H:%M:%S',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s')

log = logging.getLogger('PyATEMAPI')

# run main to start the connection and server
try:
    main()
except KeyboardInterrupt:
    log.info("Exiting from keyboard interrupt")
    switcher.disconnect()
    exit()
except Exception as e:
    log.error("An error occurred: " + str(e))
    switcher.disconnect()
    exit()
