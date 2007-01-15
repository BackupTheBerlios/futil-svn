#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

from futil.storage.shaManager import ShaManager
import unittest

import os
from pysqlite2 import dbapi2 as sqlite
TESTDB = "testfoaf.db"

SHA = "012345678901234567890123456789"
URI = "http://www.wikier.org:2080/foaf.rdf"

class TestShaManager(unittest.TestCase):

    def setUp(self):
        self.shaManager = ShaManager(TESTDB, 'test')

    # Helper method
    def insertElement(self):
        self.shaManager.insertUriSha(URI, SHA)

    def testInsertion(self):
        self.insertElement()
        self.assertTrue(len(self.shaManager.searchSha(SHA)) > 0)

    def testDuplicateInsertion(self):
        try:
            self.insertElement()
            self.insertElement()
        except sqlite.IntegrityError:
            self.assertTrue(True)

    def testSearch(self):
        self.insertElement()
        result = self.shaManager.searchSha(SHA)
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0], URI)

    def testMultipleSearch(self):   
        self.insertElement()
        result = self.shaManager.searchSha(SHA)
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0], URI)
        
        result = self.shaManager.searchSha(SHA)
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0], URI)

    def deleteDB(self):
        os.remove(TESTDB)

    def tearDown(self):
        self.deleteDB()

if __name__ == '__main__':
    unittest.main()