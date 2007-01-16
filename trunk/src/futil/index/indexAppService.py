from PyLucene import IndexWriter, IndexReader, StandardAnalyzer
from foafDocumentFactory import FoafDocumentFactory

from futil.storage.pySQLiteWrapper import PySQLiteWrapper
from futil.index.indexer import Indexer
from futil.storage.shaManager import ShaManager
from futil.utils.logger import FutilLogger
from futil.foaf.foafAnalyzer import UriLoader

class IndexAppService(Indexer):

    def __init__(self, directory, shaManager, app='futil'):
        self._directory = directory
        create = not IndexReader.indexExists(self._directory)
        self._writer = IndexWriter(self._directory, StandardAnalyzer(), create)
        self.shaBBDD = shaManager
        self.logger = FutilLogger(app)
        self.uriLoader = UriLoader(logger=self.logger)


    def indexFOAF(self, foaf):
        document = FoafDocumentFactory.getDocumentFromFOAF(foaf)
        self._writer.addDocument(document)
        if ( foaf.has_key('sha')):
            for sha in foaf['sha']:
                self.shaBBDD.insertUriSha(foaf['uri'][0], sha)

        if ( foaf.has_key('friends')):
            for friendSha, friendUri in filter( lambda x: x[0] != '', foaf['friends']):
                self.shaBBDD.insertUriSha(friendUri, friendSha)
            return [u for (v,u) in foaf['friends']]
        return []

    def indexFOAFUri(self, foafUri):
        try:
            f = self.uriLoader.getFoafFrom(foafUri)
            return self.indexFOAF(f)
        except:
            self.logger.info("Unknow error indexing " + foafUri)
            return []


    def close(self):
        if self._writer:
            self._writer.close()
        self._writer = None
        self.shaBBDD.close()