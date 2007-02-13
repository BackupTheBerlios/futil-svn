
from futil.tracker.tracker import Tracker
from futil.storage.MySQLWrapper import MySQLWrapper
from futil.utils.logger import FutilLogger

class FutilTracker(Tracker):
    
    def __init__(self, app='futil'):
        self.added = 0
        self.db = MySQLWrapper(app=app)
        self.log = FutilLogger(app)
    
    def moreUrisToExplore(self):
        return self.db.pending()
    
    def getNextUri(self):
        next = self.db.getNextPending()
        self.db.visit(next)
        return next
    
    def putFriendsUris(self, friends):
        for friend in friends:
            if (self.db.insert(friend)):
                self.added += 1
    
    def close(self):
        print self.added, 'FOAFs added'
        self.db.close()
