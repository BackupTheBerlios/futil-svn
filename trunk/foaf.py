# -*- coding: utf8 -*-
"""
 This class takes a foaf uri in constructor and builds an python object
 using SparQL. Uses reflectivity to add available properties in FOAF file.
 Probably that's not a good idea. Feel free to modify
"""

import rdflib
from rdflib.sparql import sparqlGraph
from rdflib.sparql import GraphPattern


import socket
socket.setdefaulttimeout(10)

FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
RDFS = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
RDF = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
GEO =rdflib.Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")

queries = [ ("name", ("?value"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                               ("?manfloro", FOAF['name'], "?value")])),
            ("sha", ("?value"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                              ("?manfloro", FOAF['mbox_sha1sum'], "?value")])),
            ("nick", ("?value"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                               ("?manfloro", FOAF['nick'], "?value")])),
            ("friends", ("?sha1", "?uri"), GraphPattern([("?node", FOAF["mbox_sha1sum"], "?sha1"),
                                                         ("?node", RDFS["seeAlso"], "?uri")])),
            ("geopos", ("?geolat", "?geolong"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                                              ("?manfloro", FOAF['based_near'], "?bn"),
                                                              ("?bn",GEO["lat"],"?geolat"),
                                                              ("?bn",GEO["long"],"?geolong")]))
]

class Foaf:
  

  def __init__(self, foaf=None):

    if foaf == None:
      return None
    
    if ( foaf.startswith('/')):	
      foaf = 'file://' + foaf
    
    self.uri = foaf
    
    sparqlGr = sparqlGraph.SPARQLGraph()
    sparqlGr.parse(foaf)
    for attr, select, where in queries:
      result = sparqlGr.query(select, where)
      if result == None:
        continue
      if ( len(result) == 1):
        resultlist = result[0]
      else:
        resultlist = [str(i) for i in result ]
      setattr(self, attr, resultlist)

  def __str__(self):
    text = ""
    for attr, value in self.__dict__.iteritems():
      if attr is "friends":
        continue
      text += attr + " "
      if isinstance(value, rdflib.Literal) or isinstance(value, basestring) :
        text += value.encode('utf-8') + "\n"
      else:
        text += str([i.encode('utf-8') for i in value]) + "\n"
    return text

if __name__ == "__main__":
  foaf = Foaf('http://frade.no-ip.info:2080/~ivan/foaf.rdf')
  print foaf
  foaf = Foaf('http://www.wikier.org/foaf.rdf')
  print foaf

  
