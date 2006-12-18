"""
 Interface with index operation. Each implementation choose how to handle
already existing uris
"""
class Indexer:
    
    def indexFOAFUri(self, uri):
        """
         Index FOAF in URI
        """
        pass

    def close(self):
        """
         Close indices or save data or do what you need, because crawler wants
        to finish and go to sleep.
        """
        pass
