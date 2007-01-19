
"""Script to copy our data from SQLite to MySQL"""

import sys, os
from pysqlite2 import dbapi2 as sqlite
import MySQLdb

class SQLite2MySQL:
    
    def __init__(self, sqlite, mysql):
        self.sqlite = sqlite
        self.mysql = mysql
        
    def __getFromSQLite(self):
        try:
            con = sqlite.connect(self.sqlite)
            cur = con.cursor()
            query = "SELECT * FROM foafs"
            cur.execute(query)
            tuples = cur.fetchall()
            return tuples            
        except Exception, e:
            print 'An error ocurred geting data from SQLite:', str(e)
            sys.exit(-3)        
    
    def __setToMySQL(self, tuples):
        data = { 'host':'localhost', 'db':self.mysql, 'user':'futil', 'passwd':'futil', 'table':'foafs'} 
        con = None
        try:
            con = MySQLdb.connect(host=data['host'], db=data['db'],
                                  user=data['user'], passwd=data['passwd']) 
        except MySQLdb.Error, e:
            print 'error conecting to db:', str(e[1])
            sys.exit(-4)        
        
        cur = con.cursor()
        
        copied = 0
        
        for tuple in tuples:
            uri = unicode(tuple[0])
            visited = str(int(self.__str2bool(tuple[1])))
            date = str(tuple[2])
            query = u"INSERT INTO `"+data['table']+"` (uri, visited, date) VALUES ('"+uri+"','"+visited+"',"+date+")"
            try:
                cur.execute(query)
                copied += 1
            except MySQLdb.IntegrityError, details:
                print 'Error:', uri, 'already exists on db:', str(details)
            except AssertionError, details:
                print 'Error inserting', uri + ': ' + str(details)
                sys.exit(-6)
            except Exception, details:
                #print uri, visited, date   
                print str(details)
            
        return copied
    
    def __str2bool(self, bool):
        if (bool == 'True'):
            return True
        else:
            return False
        
        
    def clone(self):
        tuples = self.__getFromSQLite()
        origSize = len(tuples)
        print origSize, 'tuples at SQLite'
        destSize = self.__setToMySQL(tuples)
        print destSize, 'tuples copied to MySQL'
        return (origSize == destSize)


if __name__ == '__main__':
    if len(sys.argv) < 3 :
        print 'Please, write the path to the original SQLite database'
        sys.exit(-1)
    else:
        orig = sys.argv[1]
        dest = sys.argv[2]
        if not os.path.exists(orig):
            print orig, 'database not founded'
            sys.exit(-2)
        else:
            sqlite2mysql = SQLite2MySQL(orig, dest)
            if sqlite2mysql.clone():
                print 'database cloned'
                sys.exit(0)
            else:
                print 'sizes are not equals'
                sys.exit(-10)

