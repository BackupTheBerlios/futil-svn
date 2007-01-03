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

class TestShaManager(unittest.TestCase):

    def setUp(self):
        self.shaManager = ShaManager(TESTDB)

    # Helper method
    def insertElement(self):
        self.shaManager.insertUriSha("http://www.wikier.org/foaf.rdf", SHA)

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

    def deleteDB(self):
        os.remove(TESTDB)

    def tearDown(self):
        self.deleteDB()

if __name__ == '__main__':
    unittest.main()