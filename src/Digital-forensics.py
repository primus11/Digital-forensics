__author__="ziga, zeljko, uros, primoz, jan"
__date__ ="$Mar 20, 2012 11:39:49 AM$"

import cherrypy
# from mako.template import Template
from mako.lookup import TemplateLookup
lookup = TemplateLookup(directories=['Templates'])

class DigitalForensics:

    def index(self):
        import subprocess
        result = subprocess.Popen('finger -l', stdout=subprocess.PIPE, shell=True)
        out = result.communicate()
        s = out[0].split('\n')

        tmpl = lookup.get_template("index.html")
        return tmpl.render(salutation="Hello", target="World", result=s)
    index.exposed = True

    def showMessage(self):
        return "Hello world!"
    showMessage.exposed = True

import os.path
conf = os.path.join(os.path.dirname(__file__), 'digital-forensics.conf')
current_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    print current_dir
    cherrypy.quickstart(DigitalForensics(), config=conf)
else:
    cherrypy.tree.mount(DigitalForensics(), config=conf)