#!/usr/bin/env python2.4

import sys
#if not '../../' in sys.path:
sys.path.append('./src')

from SOAPpy import SOAPServer
from futil.index.appfactory import appServiceFactory

WS_NS = 'http://futil.berlios.de/wsFOAF'
searcher = appServiceFactory.createSearchService()

class foafSearchWS:

    def test(self):
        return "Cadena de prueba"

    def search(self, chain):
        return searcher.search(chain)


server = SOAPServer(('', 8880))
ws = foafSearchWS()

server.registerObject(ws, WS_NS)

print "Starting server..."
server.serve_forever()