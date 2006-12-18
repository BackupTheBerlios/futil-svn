#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

from PyLucene import RAMDirectory, FSDirectory
import unittest
from futil.foaf.foaf import Foaf
from futil.index.searchAppService import SearchAppService
from futil.index.indexAppService import IndexAppService

ivan = {"name":"ivan", 
        "uri":"http://frade.no-ip.info:2080/~ivan/foaf.rdf", 
        "sha":"0123456789012345678901234567890123456789"}

sergio = {"name":"sergio", 
        "uri":"http://www.wikier.org/foaf.rdf", 
        "sha":"1123456789012345678901234567890123456789"}

class TestClientView(unittest.TestCase):


    def setUp(self):
        print "setUp"
        i = Foaf()
        i.__dict__ = ivan
        s = Foaf()
        s.__dict__ = sergio
        
        self._directory = FSDirectory.getDirectory("/tmp/borrame", True) #RAMDirectory()
        #self._directory = RAMDirectory()
        indexer = IndexAppService(self._directory)
        indexer.indexFOAF(i)
        indexer.indexFOAF(s)
        
        self._searcher = SearchAppService(self._directory)

    def testSearchByName(self):
        r = self._searcher.search("Sergio")
        self.assertEqual(len(r), 1)

    def testSearchBySha(self):
        r = self._searcher.search("0123456789012345678901234567890123456789")
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0].name, "ivan")

    def testSearchByUri(self):
        r = self._searcher.search("http://www.wikier.org/foaf.rdf")
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0].name, "sergio")

if __name__ == "__main__":
    unittest.main()
