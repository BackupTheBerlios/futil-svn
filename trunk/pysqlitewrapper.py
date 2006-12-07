#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import re
from pysqlite2 import dbapi2 as sqlite

class PySQLiteWrapper:

	def __init__(self, path="foaf.db"):
		self.path = path

	def connect(self):
		connection = sqlite.connect(self.path)
		cursor = connection.cursor()
		return cursor
	
	def query(self, uri):
		cur = self.connect()
		query = "select uri from foafs where uri =?"
		cur.execute(query, (uri,))
		return cur.fetchmany()

	def insert(self, uri, sha, me=False):
		if not self.exists(uri):
			date = "20061207"
			me = self.bool2str(me)
			cur = self.connect()
			cur.execute("insert into foafs(uri, sha, date, self) values ("+uri+","+sha+","+date+","+me+")")
		else:
			print "Error: " + uri + " already exist on db"

	def exist(self, uri):
		return (len(self.query(uri)) > 0)

	def bool2str(value):
		if (value):
			return "True"
		else:
			return "False"

	def str2bool(value):
		if (value == "True"):
			return True
		else:
			return False

	
