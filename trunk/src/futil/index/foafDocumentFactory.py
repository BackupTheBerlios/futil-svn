"""
 Factory with static methods (python equivalence) to transform
 Foaf instance in Lucene Document and inverse process
"""
from PyLucene import Document, Field
from futil.foaf.foaf import Foaf

fields = {
    "name" : ( Field.Store.YES, Field.Index.TOKENIZED),
    "nick" : ( Field.Store.YES, Field.Index.TOKENIZED),
#    "sha"  : ( Field.Store.YES, Field.Index.UN_TOKENIZED),
    "uri"  : ( Field.Store.YES, Field.Index.UN_TOKENIZED),
    "friends": (Field.Store.YES, Field.Index.UN_TOKENIZED),
    "geolat": (Field.Store.YES, Field.Index.UN_TOKENIZED),
    "geolong": (Field.Store.YES, Field.Index.UN_TOKENIZED)
}

"""
 Helper class to create static methods
 http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52304
"""
class Static:
    def __init__(self, anycallable):
        self.__call__ = anycallable


class FoafDocumentFactory:
    
    def getDocumentFromFOAF(foaf):
        doc = Document()
        for attr, value in foaf.iteritems():
            if ( fields.has_key(attr)):
                # Now is always a list!
                for x in value:
                    if isinstance(x, tuple): #for example (sha, uri)
                        doc.add(Field(attr, x[1], fields[attr][0], fields[attr][1]))
                    else:
                        doc.add(Field(attr, x, fields[attr][0], fields[attr][1]))
                
            else:
                pass
                # DEBUG information print "E: Field " + attr + " ignored in index"
        return doc
    getDocumentFromFOAF = Static(getDocumentFromFOAF)

    def getFOAFFromDocument(doc):
        f = Foaf(None)
        for key in fields.iterkeys():
            values = doc.getValues(key)
            if not values:
                continue
            if len(values) > 1:
                setattr(f, key, doc.getValues(key))
            else:
                setattr(f, key, values[0])
        return f
    getFOAFFromDocument = Static(getFOAFFromDocument)

