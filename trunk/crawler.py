import crawler
import signal, sys

import time # debug

class Crawler:
    
    def __init__(self, tracker, indexer):
        self.tracker = tracker
        self.indexer = indexer

    def start(self):
        print "Start"
        while ( self.tracker.moreUrisToExplore ) :
            uri = self.tracker.getNextUri()
            friends = self.indexer.indexURI(uri)
            self.tracker.putFriendsUris(friends)
        
    def finish(self):
        print "Finishing..."
        self.tracker.close()
        self.indexer.close()


if __name__ == "__main__":
    crawler = Crawler(None, None)  #FIXME

    def finale(a, b):
        crawler.finish()
        sys.exit(0)

    signal.signal(signal.SIGHUP, finale)
    crawler.start()