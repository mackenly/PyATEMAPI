# Filename: server.py
# Created By: Mackenly Jones on 07/12/2022
# Web: mackenly.com
# Twitter: @mackenlyjones

import argparse
import logging
import PyATEMMax
from api.Api import Api
from http.server import *

# create the switcher object
switcher = PyATEMMax.ATEMMax()
api = Api(switcher)
passphrase = 'Password1'
ip = '127.0.0.1'


class GFG(BaseHTTPRequestHandler):
    # on GET...
    def do_GET(self):
        global passphrase, ip
        if self.headers.get('Authorization') == passphrase:
            # http response code - success
            self.send_response(200)
            # http header - content type - html
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # http body - json
            self.wfile.write(bytes(str(api.get(self.path, passphrase, ip)), "utf8"))
            switcher.setProgramInputVideoSource(0, 1)
            log.info("GET request received, sent response")
        else:
            # http response code - unauthorized
            self.send_response(401)
            # http header - content type - html
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # http body - json
            self.wfile.write(b'{"error": "unauthorized"}')
            log.error("GET request received, unauthorized")
        return

    # on POST...
    def do_POST(self):
        # http response code - invalid request
        self.send_response(400)
        # http header - content type - json
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # http body - json
        self.wfile.write(b'{"error": "invalid request"}')
        log.info("POST request received, sent response")
        return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ip', help='switcher IP address')
    parser.add_argument('passphrase', help='passphrase to compare requests to', type=str, default='Password1')
    args = parser.parse_args()

    # set global variables
    global passphrase, ip
    passphrase = args.passphrase
    ip = args.ip

    log.info("Initializing switcher")
    switcher.setLogLevel(logging.INFO) # Set switcher verbosity (try DEBUG to see more)
    switcher.connect(args.ip)

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
    print("Starting server on http://localhost:" + str(port.server_port))
    port.serve_forever()


# setup logging
logging.basicConfig( datefmt='%H:%M:%S',
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s')

log = logging.getLogger('PyATEMAPI')

# run main to start the connection and server
main()
