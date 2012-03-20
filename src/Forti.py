
__author__="ziga"
__date__ ="$Mar 20, 2012 11:39:49 AM$"

import cherrypy

class Forti:

    def index(self):
        # Let's link to another method here.
        return 'We have an <a href="showMessage">important message</a> for you!'
    index.exposed = True

    def showMessage(self):
        # Here's the important message!
        return "Hello world!"
    showMessage.exposed = True

import os.path
forticonf = os.path.join(os.path.dirname(__file__), 'forti.conf')

if __name__ == "__main__":
    # CherryPy always starts with app.root when trying to map request URIs
    # to objects, so we need to mount a request handler root. A request
    # to '/' will be mapped to HelloWorld().index().
    cherrypy.quickstart(Forti(), config=forticonf)
else:
    # This branch is for the test suite; you can ignore it.
    cherrypy.tree.mount(Forti(), config=forticonf)