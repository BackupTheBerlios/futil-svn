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
        query = "select uri from foafs where uri =?"
        cur.execute(query, (uri,))
        return cur.fetchmany()


    def insert(self, uri, me=False):
        if not self.exist(uri):
            date = self.todayDate()
            me = self.bool2str(me)
            (con, cur) = self.connect()
            query = """
                        insert into foafs(uri, date, self)
                        values ('%s','%s','%s')
                    """ % (uri, date, me)
            cur.execute(query)
            con.commit()
        else:
            print "Error: " + uri + " already exist on db"

    def exist(self, uri):
        return (len(self.query(uri)) > 0)

    def bool2str(self, value):
        if (value):
            return "True"
        else:
            return "False"

    def str2bool(self, value):
        if (value == "True"):
            return True
        else:
            return False

    def todayDate(self):
        date = datetime.date.today()
        return str(date).replace("-", "")


