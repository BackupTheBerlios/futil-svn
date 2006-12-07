#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

from pysqlitewrapper import PySQLiteWrapper

if __name__ == '__main__':
	pysqlite = PySQLiteWrapper("foaf.db")
	pysqlite.query("http://www.wikier.org/foaf.rdf#wikier")
	
