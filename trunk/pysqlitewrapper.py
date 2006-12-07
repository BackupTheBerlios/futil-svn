#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

from pysqlite2 import dbapi2 as sqlite

class PySQLiteWrapper:

	def __init__(self, path="foaf.db"):
		self.path = path

	def connect(self):
		connection = sqlite.connect(self.path)
		cursor = connection.cursor()
		return cursor
	
	def query(self, value):
		field = self.findField(value)
		if (field != None):
			print field
			cur = self.connect()
			query = "select " + field + " from foafs where " + field + "=?"
			cur.execute(query, (value,))
			print cur.fetchone()
		else:
			print "unknow valye type"

	def insert(self, uri, sha, me=False):
		if not self.exists(uri, sha):
			date = "20061205"
			me = self.bool2str(me)
			cur = self.connect()
			cur.execute("insert into foafs(uri, sha, date, self) values ("+uri+","+sha+","+date+","+me+")")	
		else:
			print "Error: ("+uri+","+sha+") already exist on db"

	def exists(self, uri, sha):
		#FIXME
		return False

	def findField(self, value):
		if (value[:7] == "http://"):
			return "uri"
		elif ((len(value) == 40) and (not " " in value)):
			return "sha"
		else:
			return None

	def clear(self):
		#FIXME
		pass

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

	
