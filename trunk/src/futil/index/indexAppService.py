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
        
        if ( hasattr(foaf,'sha')):
            for sha in foaf.sha:    
                self.shaBBDD.insertUriSha(foaf.uri, sha)
                
        if ( hasattr(foaf, 'friends')):
            for friendSha, friendUri in foaf.friends:
                print "inserting ", friendSha
                self.shaBBDD.insertUriSha(friendUri, friendSha)
            return [u for (v,u) in foaf.friends]
        return []

    def indexFOAFUri(self, foafUri):
        print "Atacking ", foafUri
        f = Foaf(foafUri)
        return self.indexFOAF(f)
        
    
    def close(self):
        if self._writer:
            self._writer.close()
        self._writer = None
