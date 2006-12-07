from PyLucene import IndexWriter, IndexReader, StandardAnalyzer
from foafDocumentFactory import FoafDocumentFactory

class IndexAppService:
    
    def __init__(self, directory):
        self._directory = directory
    
    def indexFOAF(self, foaf):
        document = FoafDocumentFactory.getDocumentFromFOAF(foaf)
        writer = IndexWriter(self._directory, StandardAnalyzer(), 
            not IndexReader.indexExists(self._directory))
        writer.addDocument(document)
        writer.close()
