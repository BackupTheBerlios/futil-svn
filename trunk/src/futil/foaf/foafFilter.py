import xml.sax._exceptions
import rdflib.exceptions

foafNS = { "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                        "foaf": "http://xmlns.com/foaf/0.1/"}


class FoafFilter:

    def __init__(self, next=None):
        self.next = next

    def getFoafNS(self):
        return self.foafNS

    def run(self, data, foaf=None):
        if foaf == None:
            foaf = {}

        foaf = self.process(data, foaf)
        if ( self.next ):
            return self.next.run(data, foaf)
        return foaf


    def process(self, data, foaf):
        """
        To be implemented by subclasses
        """
        pass



    def evaluateSparQL(self, graph, select, where):
        """
         Helper method to evaluate sparQL queries
        """
        try:
            result = graph.query(select, where)
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
        c = xml.xpath.Context.Context(xmldom)
        c.setNamespaces(foafNS)
        e = xml.xpath.Compile(query)
        return e.evaluate(c)
