
# Why it doesn't works abstract class?
#    TypeError: new() takes exactly 2 arguments (3 given)
#
#from futil.utils.abstract import AbstractMethod, Metaclass
#
#"""
#    Interface to handle URIs in crawler process.
#    Implementation has complete control in which
#    URIs visit, follow, ban...
#"""
#
#class Tracker(object):
#    
#    __metaclass__ = Metaclass
#    
#    moreUrisToExplore = AbstractMethod('moreUrisToExplore')
#    getNextUri = AbstractMethod('getNextUri')
#    putFriendsUris = AbstractMethod('putFriendsUris')
#    close = AbstractMethod('close')

class Tracker:
    
    def moreUrisToExplore(self):
        pass
    
    def getNextUri(self):
        pass

    def putFriendsUris(self, friends):
        pass

    def close(self):
        pass
