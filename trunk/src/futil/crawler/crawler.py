import sys
sys.path.append('./src')


from futil.tracker.ptswtracker import PTSWTracker
from futil.index.appfactory import appServiceFactory

import signal, sys

class Crawler:
    
    def __init__(self, tracker, indexer):
        self.tracker = tracker
        self.indexer = indexer

    def start(self):
        print "Start"
        while ( self.tracker.moreUrisToExplore() ) :
            uri = self.tracker.getNextUri()
            friends = self.indexer.indexFOAFUri(uri)
            self.tracker.putFriendsUris(friends)
        
    def finish(self):
        print "Finishing..."
        self.tracker.close()
        self.indexer.close()


if __name__ == "__main__":
    
    tracker = PTSWTracker(pinged='data/initial.xml')
    indexer = appServiceFactory.createIndexService()
    crawler = Crawler(tracker, indexer)  #FIXME

    def finale(a, b):
        crawler.finish()
        sys.exit(0)

    signal.signal(signal.SIGHUP, finale)
    crawler.start()