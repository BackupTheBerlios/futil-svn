#!/usr/bin/env python2.4
# -*- coding: utf8 -*-
#
# PingTheSemanticWeb.com Wrapper
#
# http://pingthesemanticweb.com/api.php
#
# Interesant web services:
#  - All FOAFs:
#        http://pingthesemanticweb.com/export/?type=foaf&serialization=xml&timeframe=any_time&nbresults=0
#
#  - Updated FOAFs:
#        http://pingthesemanticweb.com/export/?type=foaf&serialization=all&ns=&domain=&timeframe=last_day&nbresults=0
#

import urllib2
from xml.dom import minidom

PINGED = "ptsw-foafs.xml"

class PTSW:
    
    def __init__(self):
        self.rest = "http://pingthesemanticweb.com/rest/?url="

    def ping(self, uri):
        import socket
        socket.setdefaulttimeout(10)
        response = urllib2.urlopen(self.rest+uri).read()
        responseParsed = self.__parseResponse(response)
        return (responseParsed['flerror'] == 0)

    def __alreadyPinged(self, uri):
        pass

    def __parseResponse(self, response):
        dict = {}
        dom = minidom.parseString(response)
        responses = dom.getElementsByTagName('response')
        #print response[0].getElementsByTagName('flerror')[0].firstChild.data, ' errors'
        for node in responses[0].childNodes:
            if (not node.nodeType == node.TEXT_NODE):
                key = node.nodeName
                try:
                    value = int(node.firstChild.data)
                except:
                    value = node.firstChild.data
                dict[key] = value
                    
        return dict
