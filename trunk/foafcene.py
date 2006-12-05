from PyLucene import IndexReader, IndexWriter
from PyLucene import Document, Field, StandardAnalyzer
from PyLucene import IndexSearcher, Query, TermQuery, Term
from PyLucene import RAMDirectory, FSDirectory
# from PyLucene import MultiFieldQueryParser Bug in PyLucene 2.0.0
from PyLucene import QueryParser

from array import array

from foaf import Foaf

fields = {
    "name" : ( Field.Store.YES, Field.Index.TOKENIZED),
    "nick" : ( Field.Store.YES, Field.Index.TOKENIZED),
    "sha"  : ( Field.Store.YES, Field.Index.UN_TOKENIZED)
}

class LuceneWrapper:

    def __init__(self, directory=None):
        self._indexModified = False
        self._directory = directory
        self._searcher = None

    def _prepareSearcher(self):
        if not self._searcher:
            self._searcher = IndexSearcher(self._directory)
            self._indexModified = False
            return self._searcher

        if self._indexModified:
            if self._searcher:
                self._searcher.close()
            self._searcher = IndexSearcher(self._directory)
            
        self._indexModified = False
        return self._searcher

    
    def search(self, query):
        parser = QueryParser("name", StandardAnalyzer())
        q = parser.parse(query)
        
        self._prepareSearcher()
        hits = self._searcher.search(q)

        result = []
        for i in range(0, hits.length()):
            d = hits.doc(i)
            result.append(self._getFOAFFromDocument(d))
        return result


    def _getDocumentFromFOAF(self, foaf):
        doc = Document()
        for attr, value in foaf.__dict__.iteritems():

            if ( fields.has_key(attr)):
                if isinstance(value, list):
                    for x in value:
                        doc.add(Field(attr, x, fields[attr][0], fields[attr][1]))
                else:
                    doc.add(Field(attr, value, fields[attr][0], fields[attr][1]))
            else:
                print "E: Field " + attr + " ignored in index"
        return doc

    def _getFOAFFromDocument(self, doc):
        f = Foaf(None)
        for key in fields.iterkeys():
            values = doc.getValues(key)
            if len(values) > 1:
                setattr(f, key, doc.getValues(key))
            else:
                setattr(f, key, values[0])
        return f


    def indexFOAF(self, foaf):
        document = self._getDocumentFromFOAF(foaf)
        writer = IndexWriter(self._directory, StandardAnalyzer(), True)
        writer.addDocument(document)
        writer.close()
        print "Anyadido documento"
        self._indexModified = True
        

    def close(self):
        if self._searcher:
            self._searcher.close()

if __name__ == "__main__":
    d = FSDirectory.getDirectory('/tmp/test-index',True)
    lw = LuceneWrapper(d)

    foaf = Foaf('http://frade.no-ip.info:2080/~ivan/foaf.rdf')
    lw.indexFOAF(foaf)

    foaf = Foaf('http://www.wikier.org/foaf.rdf')
    lw.indexFOAF(foaf)

    r = lw.search("sergio")
    print r[0]
    
    lw.close()

    
