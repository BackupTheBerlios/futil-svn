from futil.foaf.foafFilter import FoafFilter

from rdflib.sparql.graphPattern import GraphPattern
import rdflib

import xml

class ShaFilter(FoafFilter):
    """
     Filter to extract sha of foaf's owner
    """

    def __init__(self, next=None):
        FoafFilter.__init__(self, next)
    
        FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
        self.select = ("?value")
        self.where = GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                 ("?manfloro", FOAF['mbox_sha1sum'], "?value")])



    def tryXPath(self, xmldom):
        nodes = self.evaluateXPath(xmldom, '/rdf:RDF/foaf:Person/foaf:mbox_sha1sum/text()')
        return map(lambda x: x.toprettyxml().replace('\n',''), nodes)


    def process(self, data, foaf):
##        print "Proccessing ", self.__class__
        result = self.evaluateSparQL(data['graph'], self.select, self.where)
        if result == None or result == []:
            result = self.tryXPath(data['xmlDom'])
        foaf['sha'] = result
        return foaf