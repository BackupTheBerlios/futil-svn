import web

from SOAPpy import SOAPProxy
import socket

host = '127.0.0.1'
port = '8880'
WS_NS = 'http://futil.berlios.de/wsFOAF'

urls = (
  '/search/(.*)', 'FutilSearchREST',
  '/futil', 'Main',
  '/resources/(.*)', 'Main'
)

remote = SOAPProxy(host+':'+port, namespace=WS_NS, soapaction='', simplify_objects=1)

class FutilSearchREST:
    def GET(self, query):
        try:
            results = remote.search(query)
            for result in results:
                print result
        except socket.error, e:
            print "Launch the futil server ( futil.ws.wsServer ) and reboot web.py script"

class Main:
    def GET(self, filename=None):
        if not filename:
            print open('templates/form.html').read()
        else:
            print open('resources/' + filename).read()

#
# Web.py launch logic. Support to 0.1 and 0.2 versions
#
# Ubuntu has 0.138
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