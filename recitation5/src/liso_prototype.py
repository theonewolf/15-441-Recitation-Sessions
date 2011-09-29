#!/usr/bin/env python

import os

import datetime

import BaseHTTPServer 
import SocketServer

# hard-coded configurtion
WWW = '/tmp/www/'
PORT = 8080
MIME = {
            '.html' : 'text/html',
            '.css'  : 'text/css',
            '.png'  : 'image/png',
            '.jpg'  : 'image/jpeg',
            '.gif'  : 'image/gif'
        }

# This is the 'select()' module---except we aren't showing it here
# or actually implementing it properly
class LisoPrototype(BaseHTTPServer.HTTPServer):
    pass

# This is the HTTP/1.1 parsing module---except we don't show parsing
# only forming responses with the proper headers etc.
class LisoHandlerPrototype(BaseHTTPServer.BaseHTTPRequestHandler):
    def return404(self):
        self.send_error(404, 'Not Found')

    def return411(self):
        self.send_error(411, 'Length Required')

    def return500(self):
        self.send_error(500, 'Not Found')

    def return505(self):
        self.send_error(505, 'HTTP Version not supported')

    def check_HTTP_version(self):
        version = self.request_version.split('/')
        version = version[1].split('.')
        if version[0] != '1' or version[1] != '1':
            self.return505()
            return None

    def do_GET(self):
        self.check_HTTP_version()
        # understand requested object/URI
        URI = self.path
        full_path = os.path.normpath(WWW + URI)
        
        if os.path.isdir(full_path):
            full_path = os.path.join(full_path, 'index.html')
        
        if not os.path.exists(full_path):
            self.return404()
            return

        message_body = ''
        basename,extension = os.path.splitext(full_path)
        
        # read in full file
        try:
            datestring = os.path.getmtime(full_path)
            with open(full_path, 'r') as f:
                message_body = f.read()
        except IOError:
            self.return_500()
            return

        # format datestring
        datestring = datetime.datetime.utcfromtimestamp(datestring)
        datestring = datestring.strftime('%a, %d %b %Y %H:%M:%S GMT')

        # get proper mimetype
        try:
            mimetype = MIME[extension.lower()]
        except KeyError:
            mimetype = 'application/octet-stream'

        # send response; Server and Date headers auto-generated
        self.send_response(200, 'OK')
        self.send_header('Connection', 'close')
        self.send_header('Content-Type', mimetype)
        self.send_header('Content-Length', len(message_body))
        self.send_header('Last-Modified', datestring)
        self.end_headers()
        self.wfile.write(message_body)
        self.close_connection = 1 # hack for multi-connection browsers
        # the server above us is dumb; that's why this hack is needed

    def do_HEAD(self):
        self.check_HTTP_version()
        # understand requested object/URI
        URI = self.path
        full_path = os.path.normpath(WWW + URI)
        
        if os.path.isdir(full_path):
            full_path = os.path.join(full_path, 'index.html')
        
        if not os.path.exists(full_path):
            self.return404()

        message_body = ''
        basename,extension = os.path.splitext(full_path)
        
        # get stats
        datestring = os.path.getmtime(full_path)
        fsize = os.path.getsize(full_path)

        # format datestring
        datestring = datetime.datetime.utcfromtimestamp(datestring)
        datestring = datestring.strftime('%a, %d %b %Y %H:%M:%S %Z')

        # get proper mimetype
        try:
            mimetype = MIME[extension.lower()]
        except KeyError:
            mimetype = 'application/octet-stream'

        # send response; Server and Date headers auto-generated
        self.send_response(200, 'OK')
        self.send_header('Connection', 'close')
        self.send_header('Content-Type', mimetype)
        self.send_header('Content-Length', fsize)
        self.send_header('Last-Modified', datestring)
        self.end_headers()
        self.close_connection = 1

    def do_POST(self):
        self.check_HTTP_version()
        if 'Content-length' not in self.headers:
                return411()
                return
        self.send_response(200, 'OK')
        self.send_header('Connection', 'close')
        self.end_headers()
        self.close_connection = 1

def run():
    handler = LisoHandlerPrototype

    # set version strings for auto-generated Server header amd response
    handler.server_version = 'Liso/1.0'
    handler.sys_version = ''
    handler.protocol_version = 'HTTP/1.1'

    # server startup
    server_address = ('0.0.0.0', PORT)
    httpd = LisoPrototype(server_address, handler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
