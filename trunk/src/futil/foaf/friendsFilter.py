from futil.foaf.foafFilter import FoafFilter

from rdflib.sparql.graphPattern import GraphPattern
import rdflib

import xml

class FriendsFilter(FoafFilter):
    """
     Filter to extract friends of foaf's owner. 
    Set the result in "friends" key.
    """    
    def __init__(self, next=None):
        FoafFilter.__init__(self, next)
        
        FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
        RDFS = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
        RDF = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        self.select = ("?sha1", "?uri")
        self.where = GraphPattern([("?node", RDFS["seeAlso"], "?uri"),
                                    ("?node", RDF["type"], FOAF["Person"])])
##                                    ("?parent", RDF["type"], FOAF["Person"]),
##                                    ("?parent", RDF["knows"], "?node")])
        self.optional = GraphPattern([("?node", FOAF["mbox_sha1sum"], "?sha1")])
    
    def tryXPath(self, xmlDom, query):
        nodes = self.evaluateXPath(xmlDom, query)
        return map(lambda x: x.toprettyxml().replace('\n',''), nodes)
    
    def process(self, data, foaf):
        #print "Proccessing ", self.__class__
        result = self.evaluateSparQL(data['graph'], self.select, self.where, self.optional)
        result = [(u or '' ,v or '') for (u,v) in result]
        if result == None or result == []:
            result = self.tryXPath(data['xmlDom'], "/rdf:RDF/foaf:Person/foaf:name/text()")
        foaf['friends'] = result
        return foaf
