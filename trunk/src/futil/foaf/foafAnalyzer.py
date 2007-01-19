import sys
sys.path.append('./src')

# Filters
import futil
from futil.foaf.nameFilter import NameFilter
from futil.foaf.shaFilter import ShaFilter
from futil.foaf.friendsFilter import FriendsFilter
from futil.foaf.geoposFilter import GeoPosFilter
from futil.foaf.nickFilter import NickFilter
import urllib, urllib2
import robotparser
from urlparse import urlparse

import socket
socket.setdefaulttimeout(6)


# SparQL
import rdflib
from rdflib.sparql import sparqlGraph
from rdflib.sparql.graphPattern import GraphPattern
import xml.sax._exceptions
import rdflib.exceptions

# XML
from xml.dom import minidom
from xml import xpath

class MockLogger:
    def __init__(self):
        pass
    
    def clear(self):
        pass
    
    def info(self, message):
        print >> sys.stderr, 'INFO: ' + message
        
    def error(self, message):
        print >> sys.stderr, 'ERROR: ' + message
    
    def warn(self, message):
        print >> sys.stderr, 'WARN: ' + message



class FoafAnalyzer:
    """
     Analyzer to apply filters
    """
    def __init__(self):
        pass

    def run(self, data):
        chain = GeoPosFilter(FriendsFilter(NameFilter(ShaFilter(NickFilter()))))
        return chain.run(data)

class UriLoader:
    """
     Load an URI (local or remote) in XML-DOM and SparQL Graph formats
    """
    def __init__(self, analyzer=None, logger=None):
        self._analyzer = analyzer or FoafAnalyzer()
        self._logger = logger or MockLogger()

    def __isOnline(self, uri):
        return uri.startswith('http://')
    
    def __getBase(self, uri):
        parsed = urlparse(uri)
        base = parsed[0] + '://' + parsed[1] + '/'
        return base
        
    def __alowed(self, uri):
        base = self.__getBase(uri)
        try:
            rp = robotparser.RobotFileParser()
            rp.set_url(base + 'robots.txt')
            rp.read()
            return rp.can_fetch("*", uri)
        except Exception, e:
            self._logger.info(host + 'robots.txt not founded, assuming is allowed to crawl') 
            return True


    def __loadDocument(self, fileUri):
        if self.__isOnline( fileUri ):
            try:
                data = {}
                headers = {'Accept': 'application/rdf+xml', 
                           'User-Agent' : futil.__agent__ }
                request = urllib2.Request(fileUri, data, headers)
                text = urllib2.urlopen(request).read()
            except urllib2.HTTPError, e:
                #FIXME: try to open the urls with port using our useragent
                self._logger.error(str(e))
                text = urllib2.urlopen(fileUri).read()
        else:
            text = open(fileUri).read()

        return text

    def __getData(self, fileUri):
        
        data = {}
        
        text = self.__loadDocument(fileUri)
        
        try:
            # Load XML
            doc = minidom.parseString(text)
            data['xmlDom'] = doc
        except:
            self._logger.error(" BAD XML: " + fileUri)
            data['xmlDom'] = None
        
        try:
            # Load SparQl
            sparqlGr = sparqlGraph.SPARQLGraph()
            sparqlGr.parse(fileUri)
            data['graph'] = sparqlGr
        except:
            self._logger.error(" BAD RDF: " + fileUri)
            data['graph'] = None

        return data

    def getFoafFrom(self, uri):
        """
         Load foaf in both formats from uri and apply analyzer
        """
        
        if self.__alowed(uri):
            try:
                raw_data = self.__getData(uri)
                foaf = self._analyzer.run(raw_data)
                foaf['uri'] = [uri]
                return foaf
            except UnicodeEncodeError:
                self._logger.error("Encoding error in " + uri)
                return {}
            except Exception, e:
                # Timeout, invalid URI
                print "Exception " + str(e)
                self._logger.error("Exception " + str(e))
                return {}
        else:
            print 'No allowed to crawl', uri

if __name__ == "__main__":

    foaf = UriLoader().getFoafFrom('http://frade.no-ip.info:2080/~ivan/foaf.rdf')
    #data = UriLoader().getFoafFrom('http://www.ivan-herman.net/foaf.rdf#me')
    print foaf
