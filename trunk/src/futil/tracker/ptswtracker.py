
from futil.tracker.futiltracker import FutilTracker
from futil.utils.ptsw import PTSW
from xml.dom import minidom

class PTSWTracker(FutilTracker):
    
    def __init__(self, db='foaf.db', pinged=None):
        FutilTracker.__init__(self, db)
        self.ptsw = PTSW()
        if (pinged != None):
            uris = self.ptsw.parsePinged(pinged)
            for uri in uris:
                self.db.insert(uri)
                
    def getNextUri(self):
        next = self.db.getNextPending()
        self.db.visit(next)
        self.ptsw.ping(next)
        return next

        
        