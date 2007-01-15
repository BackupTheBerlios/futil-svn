from futil.foaf.foafFilter import FoafFilter

from rdflib.sparql.graphPattern import GraphPattern
import rdflib

import xml

class GeoPosFilter(FoafFilter):
    """
     Filter to extract geoposition of foaf's owner (if exists!)
     It sets "geolat" y "geolong" in foaf dictionary
    """

    def __init__(self, next=None):
        FoafFilter.__init__(self, next)
    
        FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
        GEO =rdflib.Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
        RDF = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
        self.select = ("?geolat", "?geolong")
        self.where = GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                    ("?manfloro", FOAF['based_near'], "?bn"),
                                    ("?bn",GEO["lat"],"?geolat"),
                                    ("?bn",GEO["long"],"?geolong")])
    
        self.relaxedWhere = GraphPattern([("?manfloro", RDF['type'], FOAF['Person']),
                                    ("?manfloro", FOAF['based_near'], "?bn"),
                                    ("?bn",GEO["lat"],"?geolat"),
                                    ("?bn",GEO["long"],"?geolong")])

    def process(self, data, foaf):
##        print "Proccessing ", self.__class__
        result = self.evaluateSparQL(data['graph'], self.select, self.where)
        if result == None or result == []:
            result = self.evaluateSparQL(data['graph'], self.select, self.relaxedWhere)
            # If somebody else has his geodata in the foaf... multiple results!
        if ( len(result) > 0 ):
            foaf['geolat'] = [result[0][0]]
            foaf['geolong'] = [result[0][1]]
        else:
            foaf['geolat'] = []
            foaf['geolong'] = []
        return foaf