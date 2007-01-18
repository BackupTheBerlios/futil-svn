
import xml.dom.minidom
from xml.dom.minidom import getDOMImplementation

#all are individual values, only 'friends' is a list
attributes = ('uri', 'name', 'sha', 'nick', 'friends', 'geolat', 'geolong')

class Foaf:
    def __init__(self, data):
        self.__dict__ = data
        
    def toxml(self):
        doc  = getDOMImplementation().createDocument(None, 'person', None)
        person = doc.documentElement
        #person.setAttribute('xmlns', "FIXME")
        
        for attr in attributes:
            if attr == 'friends':
                friends = doc.createElement(attr)
                person.appendChild(friends)
                for friend in self.__dict__[attr]:
                    node = doc.createElement('friend')
                    node.appendChild(doc.createTextNode(friend))
                    friends.appendChild(node)                    
            else:
                node = doc.createElement(attr)
                node.appendChild(doc.createTextNode(str(self.__dict__[attr])))
                person.appendChild(node)
        
        return doc
        
    def __str__(self):
        return self.toxml().toprettyxml(indent='  ', newl='\n')
