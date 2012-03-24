__author__="ziga"
__date__ ="$Mar 20, 2012 11:39:49 AM$"

import cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['Templates'])

class DigitalForensics:

    def index(self):
        tmpl = lookup.get_template("index.html")
        return tmpl.render(salutation="Hello", target="World")
    index.exposed = True

    def showMessage(self):
        return "Hello world!"
    showMessage.exposed = True

import os.path
conf = os.path.join(os.path.dirname(__file__), 'digital-forensics.conf')

if __name__ == "__main__":
    cherrypy.quickstart(DigitalForensics(), config=conf)
else:
    cherrypy.tree.mount(DigitalForensics(), config=conf)