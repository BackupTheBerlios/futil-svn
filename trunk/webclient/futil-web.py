import webpy as web

from SOAPpy import SOAPProxy
import socket

host = '127.0.0.1'
port = '8880'
WS_NS = 'http://futil.berlios.de/wsFOAF'

urls = (
  '/search/(.*)', 'FutilSearchREST',
  '/futil', 'FutilSearch',
  '/resources/(.*)', 'Resources'
)

proxy = SOAPProxy(host+':'+port, namespace=WS_NS, soapaction='', simplify_objects=1)

class FutilSearchREST:
    def GET(self, query):
        try:
            results = proxy.search(query)
            output = "<response>\n"
            for result in results:
                output += str(result)
            output += "</response>\n"    
        except socket.error, e:
            print "Launch the futil server ( futil.ws.wsServer ) and reboot web client"

class FutilSearch:
    def GET(self):
        params = web.input()
        try:
            query = params.query
            results = proxy.search(query)
            print "FIXME Draw with template in HTML %i results" %( len(results))
        except AttributeError:
            web.header("Content-Type","text/html; charset=utf-8") 
            print open('templates/form.html').read()

class Resources:
    def GET(self, filename):
        print open('resources/' + filename).read()

#
# Web.py launch logic. Support to 0.1 and 0.2 versions
#
# Ubuntu has 0.138
#
# We ship a webpy inside project. Keep this code to deliver packages ;)
#
if float(web.__version__) < 0.2 :
    web.internalerror = web.debugerror
else:
    web.webapi.internalerror = web.debugerror

if __name__ == "__main__":
    if float(web.__version__) < 0.2 :
        web.run(urls, web.reloader)
    else:
        web.run(urls, globals(), web.reloader)