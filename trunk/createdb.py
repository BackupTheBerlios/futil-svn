#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

if __name__ == '__main__':
	from pysqlite2 import dbapi2 as sqlite
	con = sqlite.connect("foaf.db")
	cur = con.cursor()
	cur.execute("create table foafs(uri, sha, date, self)")
	cur.execute("""	
					insert into foafs(uri, sha, date, self) 
					values (	'http://www.wikier.org/foaf.rdf#wikier',
								'd0fd987214f56f70b4c47fb96795f348691f93ab',
								'20061205',
								'True'
					)"""
				)
	con.commit()
