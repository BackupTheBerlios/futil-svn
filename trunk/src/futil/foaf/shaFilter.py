from futil.foaf.foafFilter import FoafFilter

from rdflib.sparql.graphPattern import GraphPattern
import rdflib

class ShaFilter(FoafFilter):
    
    def __init__(self, next=None):
        self.next = next
        if ( next ):
            FoafFilter.__init__(next)
        
        FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
        self.select = ("?value") 
        self.where = GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                 ("?manfloro", FOAF['mbox_sha1sum'], "?value")])

    def evaluateXPath(self, xmldom):
        return []


    def process(self, data, foaf):
        print "Proccessing ", self.__class__
        result = self.evaluateSparQL(data['graph'], self.select, self.where)
        if result == None or result == []:
            result = self.evaluateXPath(data['xmlDom'])
        foaf['sha'] = result
        return foaf