#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

from pysqlitewrapper import PySQLiteWrapper
import unittest

import os
from pysqlite2 import dbapi2 as sqlite
TESTDB = "testfoaf.db"

class TestPySQLite(unittest.TestCase):

    def testExist(self):
        self.insertElement()
        self.assertTrue(self.pysqlite.exist('http://www.wikier.org/foaf.rdf'))

    def testInsertion(self):
        self.pysqlite.insert('http://www.wikier.org/foaf.rdf', True)
        self.assertTrue(self.pysqlite.exist('http://www.wikier.org/foaf.rdf'))

    def deleteDB(self):
        os.remove(TESTDB)

    def insertElement(self):
        self.pysqlite.insert("http://www.wikier.org/foaf.rdf", True)

    def setUp(self):
        self.pysqlite = PySQLiteWrapper(TESTDB)

    def tearDown(self):
        self.deleteDB()

if __name__ == '__main__':
    unittest.main()


