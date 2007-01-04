
from futil.tracker.tracker import Tracker
from futil.storage.pySQLiteWrapper import PySQLiteWrapper
from futil.utils.ptsw import PTSW
from futil.utils.logger import FutilLogger

class FutilTracker(Tracker):
    
    def __init__(self, db='foaf.db'):
        self.added = 0
        self.db = PySQLiteWrapper(db)
        self.ptsw = PTSW()
        self.log = FutilLogger()
    
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
                if (not self.ptsw.ping(friend)):
                    print 'An error ocurred pinging', friend
    
    def close(self):
        print self.added, 'FOAFs added'
