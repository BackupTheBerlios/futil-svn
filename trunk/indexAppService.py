from PyLucene import IndexWriter, IndexReader, StandardAnalyzer
from foafDocumentFactory import FoafDocumentFactory

from pysqlitewrapper import PySQLiteWrapper
from foaf import Foaf

class IndexAppService:
    
    def __init__(self, directory):
        self._directory = directory
        self._writer = None
        self.bbdd = PySQLiteWrapper()

    def _prepareWriter(self):
        print "First prepare writer"
        if not self._writer:
            create = not IndexReader.indexExists(self._directory)
            self._writer = IndexWriter(self._directory, StandardAnalyzer(), True)
        return self._writer

    def _closeWriter(self):
        if self._writer:
            self._writer.close()
        self._writer = None
    
    def _indexFOAF(self, foaf):
        document = FoafDocumentFactory.getDocumentFromFOAF(foaf)
        self._prepareWriter().addDocument(document)

    def recursiveIndexFOAFUri(self, initialFoafUri):
        pending = [initialFoafUri]
        for p in pending:
            pending.append(self.indexFOAFUri(p))

    def indexFOAFUri(self, foafUri):
        print "Atacking ", foafUri
        f = Foaf(foafUri)
        if not self.bbdd.exist(f.uri):
            print "Adding it to database"
            self._indexFOAF(f)
            self.bbdd.insert(f.uri, True)
            for friendSha, friendUri in f.friends:
                self.bbdd.insert(friendUri, False)
        return [u for (v,u) in f.friends]