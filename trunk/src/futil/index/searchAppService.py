from PyLucene import StandardAnalyzer, KeywordAnalyzer
from PyLucene import IndexSearcher
from PyLucene import QueryParser

from foafDocumentFactory import FoafDocumentFactory

class SearchAppService:
    
    def __init__(self, directory):
        self._directory = directory
        self._searcher = IndexSearcher(self._directory)
    
    def _prepareSearcher(self):
        # TODO: test index.currentVersion to update searcher,
        # allowing concurrence in search and write
        if self._searcher:
            self._searcher.close()
        self._searcher = IndexSearcher(self._directory)
    
    def search(self, query):
        import re
        if  re.match("^[a-f0-9]{40}$", query):
            return self.searchBySHA(query)
        elif query.startswith("http://"):
            return self.searchByURI(query)
        else:
            return self.searchByName(query)
    
    def searchByURI(self, query):
        print "Searching by URI"
        query = "\"" + query + "\""
        parser = QueryParser("uri", KeywordAnalyzer())
        return self._performSearch(parser, query)
    
    def searchByName(self, query):
        print "Preguntando por nombre"
        parser = QueryParser("name", StandardAnalyzer())
        return self._performSearch(parser, query)

    def searchBySHA(self, query):
        print "Preguntando por SHA"
        parser = QueryParser("sha", StandardAnalyzer())
        return self._performSearch(parser, query)

    def _performSearch(self, queryParser,query):
        q = queryParser.parse(query)
        
        self._prepareSearcher()
        hits = self._searcher.search(q)
        result = []
        for i in range(0, hits.length()):
            d = hits.doc(i)
            result.append(FoafDocumentFactory.getFOAFFromDocument(d))
        return result
