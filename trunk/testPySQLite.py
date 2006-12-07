#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

from pysqlitewrapper import PySQLiteWrapper
import unittest

import os
from pysqlite2 import dbapi2 as sqlite
TESTDB = "testfoaf.db"

class TestPySQLite(unittest.TestCase):

    def createEmptyDB(self):
        con = sqlite.connect(TESTDB)
        cur = con.cursor()
        cur.execute("create table foafs(uri, date, self)")
        con.close()

    def deleteDB(self):
        os.remove(TESTDB)

    def insertElement(self):
        con = sqlite.connect(TESTDB)
        cur = con.cursor()
        cur.execute("""	
                        insert into foafs(uri, date, self) 
                        values ('http://www.wikier.org/foaf.rdf#wikier','20061207','True')
                    """)
        con.commit()
        con.close()

    def setUp(self):
        self.createEmptyDB()
        self.pysqlite = PySQLiteWrapper("foaf.db")

    def tearDown(self):
        print "Tear down"
        self.deleteDB()

    def testExist(self):
        self.insertElement()
        self.assertEqual(self.pysqlite.exist("http://www.wikier.org/foaf.rdf#wikier"), True)

if __name__ == '__main__':
	unittest.main()
	
