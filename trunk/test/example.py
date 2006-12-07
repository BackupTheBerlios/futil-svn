#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

from pysqlitewrapper import PySQLiteWrapper

if __name__ == '__main__':
	pysqlite = PySQLiteWrapper("foaf.db")
	pysqlite.query("d0fd987214f56f70b4c47fb96795f348691f93ab")
	
