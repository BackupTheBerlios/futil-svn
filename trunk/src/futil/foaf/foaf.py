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
import urllib2

#from futil.utils.logger import FutilLogger

import socket
socket.setdefaulttimeout(10)

import libxml2


FOAF = rdflib.Namespace("http://xmlns.com/foaf/0.1/")
RDFS = rdflib.Namespace("http://www.w3.org/2000/01/rdf-schema#")
RDF = rdflib.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
GEO =rdflib.Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")

queries = [ ("name", ("?value"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                               ("?manfloro", FOAF['name'], "?value")]),
                                            "/RDF:rdf/foaf:Person/foaf:name"),
            ("sha", ("?value"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                              ("?manfloro", FOAF['mbox_sha1sum'], "?value")]), None),
            ("nick", ("?value"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                               ("?manfloro", FOAF['nick'], "?value")]), None),
            ("friends", ("?sha1", "?uri"), GraphPattern([("?node", FOAF["mbox_sha1sum"], "?sha1"),
                                                         ("?node", RDFS["seeAlso"], "?uri")]), None),
            ("geopos", ("?geolat", "?geolong"), GraphPattern([("?node", FOAF['maker'], "?manfloro"),
                                                              ("?manfloro", FOAF['based_near'], "?bn"),
                                                              ("?bn",GEO["lat"],"?geolat"),
                                                              ("?bn",GEO["long"],"?geolong")]), None)
]

xpaths = [
    ("name", )
]


class ErroneousFoaf(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class Foaf:

  def tryXpath(self, uri, xpath):
    print "Trying xpath: ", xpath
    if xpath == None:
        return None

    if uri.startswith('http'):
        doc = libxml2.parseUri(uri)
    else:
        file = open(uri[7:]).read()
        doc = libxml2.parseDoc(file)

    for result in doc.xpathEval(xpath):
        print "Result xpath: "#, result
    return None

  def __init__(self, foafUri=None):
##    self.log = FutilLogger()
    try:
        if foafUri == None:
          return None

        if ( foafUri.startswith('/')):
          foafUri = 'file://' + foafUri

        self.uri = foafUri

        sparqlGr = sparqlGraph.SPARQLGraph()
        sparqlGr.parse(foafUri)

        for attr, select, where, xpath in queries:
          result = sparqlGr.query(select, where)
          if result == None or result == []:
          #  result = self.tryXpath(foafUri, xpath)
          #if result == None:
            continue
          setattr(self, attr, result)
    except urllib2.URLError:
        print >> sys.stderr , " URL exception: ", foafUri          
    except xml.sax._exceptions.SAXParseException:
        print >> sys.stderr , " BAD XML: ", foafUri
##        self.log.error(" BAD XML: " + foafUri)
        raise ErroneousFoaf(foafUri)
    except rdflib.exceptions.ParserError:
        print >> sys.stderr , " BAD RDF: ", foafUri
##        self.log.error(" BAD RDF: " + foafUri)
        raise ErroneousFoaf(foafUri)
    except UnicodeEncodeError:
        print >> sys.stderr , "Encoding error in ", foafUri
##        self.log.error("Encoding error in " + foafUri)
        raise ErroneousFoaf(foafUri)
##    except Exception, e:
##        print >> sys.stderr , "Something really strange with ", foafUri, str(e)
####        self.log.error("Encoding error in " + foafUri)
##        raise ErroneousFoaf(foafUri)

  def __str__(self):
    text = ""
    for attr, value in self.__dict__.iteritems():
      if attr is "friends":
        continue
      text += attr + " "
      if isinstance(value, rdflib.Literal) or isinstance(value, basestring) :
        text += value.encode('utf-8') + "\n"
      else:
        if len(value) > 0 and not isinstance(value[0], tuple):
            text += str([i.encode('utf-8') for i in value]) + "\n"
        else:
            print "GRRRR " + attr + " - "+ str(value)
    return text

if __name__ == "__main__":
  foaf = Foaf('http://frade.no-ip.info:2080/~ivan/foaf.rdf')
  print foaf
  foaf = Foaf('http://www.wikier.org/foaf.rdf')
  print foaf
  foaf = Foaf('noexiste.org')
  print foaf


