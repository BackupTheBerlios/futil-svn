#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import re
from pysqlite2 import dbapi2 as sqlite
import datetime

class PySQLiteWrapper:

    def __init__(self, path="foaf.db"):
        self.path = path

    def connect(self):
        connection = sqlite.connect(self.path)
        cursor = connection.cursor()
        return (connection,cursor)

    def query(self, uri):
        con, cur = self.connect()
        query = "SELECT uri FROM foafs WHERE uri =?"
        cur.execute(query, (uri,))
        return cur.fetchmany()


    def insert(self, uri, me=False):
        if not self.exist(uri):
            date = self.todayDate()
            (con, cur) = self.connect()
            query = """
                        INSERT INTO foafs(uri, date, self)
                        VALUES ('%s','%s','%s')
                    """ % (uri, date, me)
            cur.execute(query)
            con.commit()
        else:
            print "Error: " + uri + " already exist on db"

    def exist(self, uri):
        return (len(self.query(uri)) > 0)

    def todayDate(self):
        date = datetime.date.today()
        return str(date).replace("-", "")


