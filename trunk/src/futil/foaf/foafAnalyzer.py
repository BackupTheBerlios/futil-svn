import sys
sys.path.append('./src')

# Filters
from futil.foaf.nameFilter import NameFilter
from futil.foaf.shaFilter import ShaFilter
from futil.foaf.friendsFilter import FriendsFilter
import urllib2

# SparQL
import rdflib
from rdflib.sparql import sparqlGraph
from rdflib.sparql.graphPattern import GraphPattern

# XML
from xml.dom import minidom
from xml import xpath


class FoafAnalyzer:
    """
     Analyzer to apply filters
    """
    def __init__(self):
        pass

    def run(self, data):
        chain = FriendsFilter(NameFilter(ShaFilter()))
        return chain.run(data)


class UriLoader:
    """
     Load an URI (local or remote) in XML-DOM and SparQL Graph formats
    """
    def __init__(self, analyzer=None):
        self._analyzer = analyzer or FoafAnalyzer()

    def __isOnline(self, uri):
        return uri.startswith('http://')


    def __getData(self, fileUri):
        data = {}

        if self.__isOnline( fileUri ):
            text = urllib2.urlopen(fileUri).read()
        else:
            text = open(fileUri).read()

        # Load XML
        doc = minidom.parseString(text)
        data['xmlDom'] = doc

        # Load SparQl
        sparqlGr = sparqlGraph.SPARQLGraph()
        sparqlGr.parse(fileUri)
        data['graph'] = sparqlGr

        return data

    def getFoafFrom(self, uri):
        """
         Load foaf in both formats from uri and apply analyzer
        """
        raw_data = self.__getData(uri)
        return self._analyzer.run(raw_data)

if __name__ == "__main__":

    foaf = UriLoader().getFoafFrom('http://frade.no-ip.info:2080/~ivan/foaf.rdf')
    #data = UriLoader().getFoafFrom('http://www.ivan-herman.net/foaf.rdf#me')
    print foaf
