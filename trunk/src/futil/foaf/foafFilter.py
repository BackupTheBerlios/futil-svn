import xml.sax._exceptions
import rdflib.exceptions

foafNS = {  "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "foaf": "http://xmlns.com/foaf/0.1/"}


class FoafFilter:

    def __init__(self, next):
        """
         next: Following filter, subclass of FoafFilter
        """
        self.next = next

    def run(self, data, foaf=None):
        """
         "Chain of responsability" iteration method
        """
        if foaf == None:
            foaf = {}

        foaf = self.process(data, foaf)
        if ( self.next ):
            return self.next.run(data, foaf)
        return foaf


    def process(self, data, foaf):
        """
        To be implemented by subclasses
         data: dictionary with foaf in sparqlgraph and xml DOM formats
         foaf: dictionary. Each filter will add a new key with appropiate
          contents
        """
        pass



    def evaluateSparQL(self, graph, select, where, optional=None):
        """
         Helper method to evaluate sparQL queries
        """
        try:
            result = graph.query(select, where, optional)
            return result
        except xml.sax._exceptions.SAXParseException:
            print >> sys.stderr , " BAD XML: ", foafUri
            return None
        except rdflib.exceptions.ParserError:
            print >> sys.stderr , " BAD RDF: ", foafUri
            return None
        except UnicodeEncodeError:
            print >> sys.stderr , "Encoding error in ", foafUri
            return None

    def evaluateXPath(self, xmldom, query):
        """
         Helper method to evaluate xpath queries
        """
        c = xml.xpath.Context.Context(xmldom)
        c.setNamespaces(foafNS)
        e = xml.xpath.Compile(query)
        return e.evaluate(c)
