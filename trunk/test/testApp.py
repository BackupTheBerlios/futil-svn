#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

import os
from PyLucene import RAMDirectory, FSDirectory
import unittest
from futil.index.searchAppService import SearchAppService
from futil.index.indexAppService import IndexAppService
from futil.storage.shaManager import ShaManager

TESTDB = "shas.TEST.db"

FRADEURI = "http://frade.no-ip.info:2080/~ivan/foaf.rdf"
WIKIERURI = "http://www.wikier.org/foaf.rdf"
NOEXISTE = "http://www.frikier.org/foaf.rdf"

class TestClientView(unittest.TestCase):


    def setUp(self):

        self._directory = RAMDirectory()
        self.shaManager = ShaManager(TESTDB)
        indexer = IndexAppService(self._directory, self.shaManager)
        indexer.indexFOAFUri(FRADEURI)
        indexer.indexFOAFUri(WIKIERURI)
        indexer.close()

        self._searcher = SearchAppService(self._directory, self.shaManager)

    def testSearchByName(self):
        r = self._searcher.search("Sergio")
        self.assertEqual(len(r), 1)

    def testSearchBySha(self):
        r = self._searcher.search("84d076726727b596b08198e26ef37e4817353e97")
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0]['name'], u'Ivan Frade')

    def testSearchByShaNoExists(self):
        r = self._searcher.search("0123456789012345678901234567890123456xxx")
        self.assertEqual(len(r), 0)

    def testSearchByUri(self):
        r = self._searcher.search("http://www.wikier.org/foaf.rdf")
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0]['name'], u'Sergio Fernández')

    def testIndexBadUri(self):
        try:
            indexer = IndexAppService(self._directory, self.shaManager)
            indexer.indexFOAFUri("http://www.frikier.org/noexiste.rdf")
            indexer.close()
        finally:
            indexer.close()

    def testOptimization(self):
        indexer = IndexAppService(self._directory, self.shaManager)
        self.assertEquals(indexer.counter, 1000)
        for i in range(0,100):
            indexer.indexFOAF({"sha":"xxxxxxx", "uri":"http://www.blablabla.org"})
        self.assertEquals(indexer.counter, 900)

        indexer.counter = 5
        for i in range(0,6):
            indexer.indexFOAF({"sha":"xxxxxxx", "uri":"http://www.blablabla.org"})
        self.assertEquals(indexer.counter, 999)

    def tearDown(self):
        self.shaManager.printDatabase()
        self._searcher.close()
        self.shaManager.close()
        #os.remove(TESTDB)

if __name__ == "__main__":
    unittest.main()
