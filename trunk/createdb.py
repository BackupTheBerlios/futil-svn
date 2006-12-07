#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

if __name__ == '__main__':
	from pysqlite2 import dbapi2 as sqlite
	con = sqlite.connect("foaf.db")
	cur = con.cursor()
	cur.execute("create table foafs(uri, date, self)")
	cur.execute("""	
					insert into foafs(uri, date, self) 
					values ('http://www.wikier.org/foaf.rdf#wikier','20061207','True')
				""")
	con.commit()
