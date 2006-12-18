from PyLucene import IndexWriter, IndexReader, StandardAnalyzer
from foafDocumentFactory import FoafDocumentFactory

from futil.storage.pySQLiteWrapper import PySQLiteWrapper
from futil.foaf.foaf import Foaf
from futil.index.indexer import Indexer

class IndexAppService(Indexer):
    
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
    
    def indexFOAF(self, foaf):
        document = FoafDocumentFactory.getDocumentFromFOAF(foaf)
        self._prepareWriter().addDocument(document)

    def recursiveIndexFOAFUri(self, initialFoafUri):
        pending = [initialFoafUri]
        for p in pending:
            pending.append(self.indexFOAFUri(p))

    def indexFOAFUri(self, foafUri):
        print "Atacking ", foafUri
        f = Foaf(foafUri)
        if not self.bbdd.exists(f.uri):
            print "Adding it to database"
            self.indexFOAF(f)
            self.bbdd.insert(f.uri, True)
            for friendSha, friendUri in f.friends:
                self.bbdd.insert(friendUri, False)
        return [u for (v,u) in f.friends]
    
    def close(self):
        self._closeWriter()
