attributes = ('name', 'sha', 'friends', 'nick', 'uri', 'geolat', 'geolong')


class Foaf:
    def __init__(self, data):
        self.__dict__ = data
        
    def __str__(self):
        pass