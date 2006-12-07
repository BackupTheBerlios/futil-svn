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
        self.assertEqual(self.pysqlite.exist('http://www.wikier.org/foaf.rdf'), True)

    def testInsertion(self):
        self.pysqlite.insert('http://www.wikier.org/foaf.rdf', True)
        self.assertEqual(self.pysqlite.exist("http://www.wikier.org/foaf.rdf"), True)

    def createEmptyDB(self):
        print "Creando DDBB vacia"
        con = sqlite.connect(TESTDB)
        cur = con.cursor()
        cur.execute("create table foafs(uri, date, self)")
        con.commit()
        con.close()

    def deleteDB(self):
        os.remove(TESTDB)

    def insertElement(self):
        print "Insertando elemento"
        con = sqlite.connect(TESTDB)
        cur = con.cursor()
        cur.execute("""	
                        insert into foafs(uri, date, self) 
                        values ('http://www.wikier.org/foaf.rdf','20061207','True')
                    """)
        con.commit()
        con.close()

    def setUp(self):
        self.createEmptyDB()
        self.pysqlite = PySQLiteWrapper(TESTDB)

    def tearDown(self):
        self.deleteDB()


if __name__ == '__main__':
	unittest.main()
	
