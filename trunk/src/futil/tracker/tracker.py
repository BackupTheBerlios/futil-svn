from futil.utils.abstract import AbstractMethod, Metaclass

"""
    Interface to handle URIs in crawler process.
    Implementation has complete control in which
    URIs visit, follow, ban...
"""

class Tracker(object):
    
    __metaclass__ = Metaclass
    
    moreUrisToExplore = AbstractMethod('moreUrisToExplore')
    getNextUri = AbstractMethod('getNextUri')
    putFriendsUris = AbstractMethod('putFriendsUris')
    close = AbstractMethod('close')

