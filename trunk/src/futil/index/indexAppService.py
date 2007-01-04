from PyLucene import IndexWriter, IndexReader, StandardAnalyzer
from foafDocumentFactory import FoafDocumentFactory

from futil.storage.pySQLiteWrapper import PySQLiteWrapper
from futil.foaf.foaf import Foaf, ErroneousFoaf
from futil.index.indexer import Indexer
from futil.storage.shaManager import ShaManager
from futil.utils.logger import FutilLogger


class IndexAppService(Indexer):
    
    def __init__(self, directory, shaManager):
        self._directory = directory
        create = not IndexReader.indexExists(self._directory)
        self._writer = IndexWriter(self._directory, StandardAnalyzer(), create)
        self.shaBBDD = shaManager
        self.logger = FutilLogger()

   
    def indexFOAF(self, foaf):
        document = FoafDocumentFactory.getDocumentFromFOAF(foaf)
        self._writer.addDocument(document)
        
        if ( hasattr(foaf,'sha')):
            for sha in foaf.sha:    
                self.shaBBDD.insertUriSha(foaf.uri, sha)
                
        if ( hasattr(foaf, 'friends')):
            for friendSha, friendUri in foaf.friends:
                self.shaBBDD.insertUriSha(friendUri, friendSha)
            return [u for (v,u) in foaf.friends]
        return []

    def indexFOAFUri(self, foafUri):
        try: 
            f = Foaf(foafUri)
            return self.indexFOAF(f)
        except ErroneousFoaf, e:
            self.logger.info("Error parsing FOAF: " + foafUri + " - " + e)
            return []
        except:
            self.logger.info("Unknow error indexing " + foafUri)
            return []
        
    
    def close(self):
        if self._writer:
            self._writer.close()
        self._writer = None
        self.shaBBDD.close()