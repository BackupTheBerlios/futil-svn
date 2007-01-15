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


ivan = {"name":["ivan"],
        "uri":["http://frade.no-ip.info:2080/~ivan/foaf.rdf"],
        "sha":["0123456789012345678901234567890123456789"],
        "friends":[("0123456789012345678901234567890123456111", "http://blabal"),
                    ("0123456789012345678901234567890123456000", "http://blaba3")]}

sergio = {"name":["sergio"],
        "uri":["http://www.wikier.org/foaf.rdf"],
        "sha":["1123456789012345678901234567890123456789"]}

TESTFILE = "data/test/frade.rdf"

class TestClientView(unittest.TestCase):


    def setUp(self):

        self._directory = RAMDirectory()
        self.shaManager = ShaManager(TESTDB)
        indexer = IndexAppService(self._directory, self.shaManager)
        indexer.indexFOAF(ivan)
        indexer.indexFOAF(sergio)
        indexer.close()

        self._searcher = SearchAppService(self._directory, self.shaManager)

    def testSearchByName(self):
        r = self._searcher.search("Sergio")
        self.assertEqual(len(r), 1)

    def testSearchBySha(self):
        r = self._searcher.search("0123456789012345678901234567890123456789")
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0]['name'], "ivan")

    def testSearchByShaNoExists(self):
        r = self._searcher.search("0123456789012345678901234567890123456xxx")
        self.assertEqual(len(r), 0)

    def testSearchByUri(self):
        r = self._searcher.search("http://www.wikier.org/foaf.rdf")
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0]['name'], "sergio")

    def printDatabase(self):
        self.shaManager.printDatabase()

    def tearDown(self):
        self._searcher.close()
        self.shaManager.close()
        os.remove(TESTDB)

if __name__ == "__main__":
    unittest.main()
