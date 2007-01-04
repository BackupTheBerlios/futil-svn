# -*- coding: utf8 -*-
"""
 This class takes a foaf uri in constructor and builds an python object
 using SparQL. Uses reflectivity to add available properties in FOAF file.
 Probably that's not a good idea. Feel free to modify
"""

import rdflib
from rdflib.sparql import sparqlGraph
from rdflib.sparql.graphPattern import GraphPattern
import os, sys, foaf
import xml.sax._exceptions
import rdflib.exceptions


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


class ErroneousFoaf(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)     

class Foaf:
  

  def __init__(self, foafUri=None):

    try:
        if foafUri == None:
          return None
        
        if ( foafUri.startswith('/')):	
          foafUri = 'file://' + foafUri
        
        self.uri = foafUri
        
        sparqlGr = sparqlGraph.SPARQLGraph()
        sparqlGr.parse(foafUri)
            
        for attr, select, where in queries:
          result = sparqlGr.query(select, where)
          if result == None:
            continue
          setattr(self, attr, result)
    except xml.sax._exceptions.SAXParseException:
        print >> sys.stderr , " BAD XML: ", foafUri
        raise ErroneousFoaf(foafUri)
    except rdflib.exceptions.ParserError:
        print >> sys.stderr , " BAD RDF: ", foafUri
        raise ErroneousFoaf(foafUri)
    except UnicodeEncodeError:
        print >> sys.stderr , "Encoding error in ", foafUri
        raise ErroneousFoaf(foafUri)
    except Exception:
        print >> sys.stderr , "Something really strange with ", foafUri
        raise ErroneousFoaf(foafUri)
    
  def __str__(self):
    text = ""
    for attr, value in self.__dict__.iteritems():
      if attr is "friends":
        continue
      text += attr + " "
      if isinstance(value, rdflib.Literal) or isinstance(value, basestring) :
        text += value.encode('utf-8') + "\n"
      else:
        if not isinstance(value[0], tuple):
            text += str([i.encode('utf-8') for i in value]) + "\n"
    return text

if __name__ == "__main__":
  foaf = Foaf('http://frade.no-ip.info:2080/~ivan/foaf.rdf')
  print foaf
  foaf = Foaf('http://www.wikier.org/foaf.rdf')
  print foaf
  foaf = Foaf('noexiste.org')
  print foaf

  
