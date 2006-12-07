#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

from pysqlitewrapper import PySQLiteWrapper
import unittest

class TestPySQLite(unittest.TestCase):

    def setUp(self):
        self.pysqlite = PySQLiteWrapper("foaf.db")

    def testCreation(self):
		print self.pysqlite
		self.assertEqual(self.pysqlite.exist("http://www.wikier.org/foaf.rdf#wikier"), True)

if __name__ == '__main__':
	unittest.main()
	
