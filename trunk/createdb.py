#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys

if __name__ == '__main__':
    if ( not len(sys.argv) == 2 ):
        print "Usage: ./createdb filename"
        sys.exit(-1)
        
    from pysqlite2 import dbapi2 as sqlite
    print "Creating database in", sys.argv[1]
    con = sqlite.connect(sys.argv[1])
    cur = con.cursor()
    cur.execute("CREATE TABLE foafs (uri TEXT PRIMARY KEY, date TEXT, self BOOL)")
    con.commit()
