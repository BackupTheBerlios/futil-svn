
import xml.dom.minidom
from xml.dom.minidom import getDOMImplementation

attributes = ('uri', 'name', 'sha', 'nick', 'friends', 'geolat', 'geolong')

class Foaf:
    def __init__(self, data):
        self.__dict__ = data

    def toxml(self):
        doc = getDOMImplementation().createDocument(None, 'person', None)
        person = doc.documentElement
        #person.setAttribute('xmlns', "FIXME")

        for attr in attributes:
            try:
                values = self.__dict__[attr]
                for value in values:
                    node = doc.createElement(attr)
                    node.appendChild(doc.createTextNode(str(value)))
                    person.appendChild(node)
            except:
                node = doc.createElement(attr)
                person.appendChild(node)

        return person

##    def __str__(self):
##        return self.toxml().toprettyxml(indent='  ', newl='\n')


def foafs2xml(foafs):
    doc = getDOMImplementation().createDocument(None, 'response', None)
    response = doc.documentElement

    for foaf in foafs:
        response.appendChild(Foaf(foaf).toxml().cloneNode(True))

    return doc.toprettyxml(indent='  ', newl='\n')
