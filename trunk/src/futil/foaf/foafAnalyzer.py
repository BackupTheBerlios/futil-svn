import sys
sys.path.append('./src')
from futil.foaf.nameFilter import NameFilter
from futil.foaf.shaFilter import ShaFilter

import urllib2

# SparQL
import rdflib
from rdflib.sparql import sparqlGraph
from rdflib.sparql.graphPattern import GraphPattern

# XML
from xml.dom import minidom
from xml import xpath


class FoafAnalyzer:
    
    def __init__(self):
        pass
        
    def run(self, data):
        chain = ShaFilter(NameFilter())
        return chain.run(data)



class UriLoader:
    def __init__(self):
        pass
        
    def isOnline(self, uri):
        return uri.startswith('http://')
    
   
    def getData(self, fileUri):
        data = {}
        
        if self.isOnline( fileUri ):
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


if __name__ == "__main__":
   
##    data = UriLoader().getData('http://frade.no-ip.info:2080/~ivan/foaf.rdf')
    data = UriLoader().getData('http://www.ivan-herman.net/foaf.rdf#me')
    print data
    a = FoafAnalyzer()
    print a.run(data)