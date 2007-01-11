from futil.foaf.foafFilter import FoafFilter

from rdflib.sparql.graphPattern import GraphPattern
import rdflib

import xml

class NameFilter(FoafFilter):
    
    def __init__(self, next=None):
        self.next = next
        if ( next ):
            FoafFilter.__init__(next)
        
        FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
        self.select = ("?value")
        self.where = GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                    ("?manfloro", FOAF['name'], "?value")])
    
    def tryXPath(self, xmlDom, query):
        nodes = self.evaluateXPath(xmlDom, query)
        return map(lambda x: x.toprettyxml().replace('\n',''), nodes)
    
    def process(self, data, foaf):
        print "Proccessing ", self.__class__
        result = self.evaluateSparQL(data['graph'], self.select, self.where)
        if result == None or result == []:
            result = self.tryXPath(data['xmlDom'], "/rdf:RDF/foaf:Person/foaf:name/text()")
        foaf['name'] = result
        return foaf
