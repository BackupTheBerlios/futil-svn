"""
    Interface to handle URIs in crawler process.
    Implementation has complete control in which
    URIs visit, follow, ban...
"""

class Tracker:
    
    def moreUrisToExplore(self):
        """
         Return a boolean indicating if there are pending URIs to explore
        """
        pass
    
    def getNextUri(self):
        """
         Following URI
        """
        pass
    
    def putFriendsUris(self, friends):
        """
         Friends of the last visited URI
        """
        pass
    
    def close(self):
        """
         Save data to resumen process, because crawler wants to finish
        """
        pass
