
from futil.tracker.futiltracker import FutilTracker
from xml.dom import minidom

class PTSWTracker(FutilTracker):
    
    def __init__(self, db='foaf.db', pinged=None):
        FutilTracker.__init__(self, db)
        
        if (pinged != None):
            uris = self.ptsw.parsePinged(pinged)
            for uri in uris:
                self.db.insert(uri)

        
        