from PyLucene import IndexWriter, IndexReader, StandardAnalyzer
from foafDocumentFactory import FoafDocumentFactory

from futil.storage.pySQLiteWrapper import PySQLiteWrapper
from futil.foaf.foaf import Foaf
from futil.index.indexer import Indexer
from futil.storage.shaManager import ShaManager

class IndexAppService(Indexer):
    
    def __init__(self, directory, shaManager):
        self._directory = directory
        create = not IndexReader.indexExists(self._directory)
        self._writer = IndexWriter(self._directory, StandardAnalyzer(), create)
        self.shaBBDD = shaManager

   
    def indexFOAF(self, foaf):
        document = FoafDocumentFactory.getDocumentFromFOAF(foaf)
        self._writer.addDocument(document)

    def indexFOAFUri(self, foafUri):
        print "Atacking ", foafUri
        f = Foaf(foafUri)
        self.indexFOAF(f)
        for friendSha, friendUri in f.friends:
            self.shaBBDD.insertUriSha(friendUri, friendSha)
        return [u for (v,u) in f.friends]
    
    def close(self):
        if self._writer:
            self._writer.close()
        self._writer = None
