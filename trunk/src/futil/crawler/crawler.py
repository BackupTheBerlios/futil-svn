import sys
sys.path.append('./src')

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
        self.close()
    
    def close(self):
        self.tracker.close()
        self.indexer.close()

    def finish(self):
        print "Finishing..."
        self.close()
