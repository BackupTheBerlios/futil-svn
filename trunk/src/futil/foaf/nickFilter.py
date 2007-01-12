from futil.foaf.foafFilter import FoafFilter

from rdflib.sparql.graphPattern import GraphPattern
import rdflib

import xml

class NickFilter(FoafFilter):
    """
     Filter to extract nick of foaf's owner. Set the result in "nick" key.
    """

    def __init__(self, next=None):
        FoafFilter.__init__(self, next)
    
        FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
        self.select = ("?value")
        self.where = GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                    ("?manfloro", FOAF['nick'], "?value")])



    def process(self, data, foaf):
##        print "Proccessing ", self.__class__
        result = self.evaluateSparQL(data['graph'], self.select, self.where)
        foaf['nick'] = result
        return foaf