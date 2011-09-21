#!/usr/bin/env python
###############################################################################
#                                                                             #
#   This script implements a simple example webserver, taken from             #
#   flask.pocoo.org.                                                          #
#                                                                             #
#   It is an example script for Recitation 4 of 15-441                        #
#                                                                             #
#   Author: Wolfgang Richter <wolf@cs.cmu.edu>                                #
#                                                                             #
###############################################################################


# flask is our web framework of choice, see flask.pocoo.org for documentation
from flask import Flask
app = Flask(__name__)

# this creates a root handler; anything returned goes straight to the client
@app.route("/")
def hello():
    """Return a Hello, World Flask example root site."""
    return "Hello World!"


# only run if running as main() (executed directly)
# commonly used in development to run a built-in web server
if __name__ == "__main__":
    app.run()
