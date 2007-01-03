#!/usr/bin/env python2.4
# -*- coding: utf8 -*-
#
# PingTheSemanticWeb.com Wrapper
#
# http://pingthesemanticweb.com/api.php
#
# Interesant web services:
#  - All FOAFs:
#        http://pingthesemanticweb.com/export/?type=foaf&timeframe=any_time&nbresults=0
#
#  - Updated FOAFs:
#        http://pingthesemanticweb.com/export/?type=foaf&serialization=all&ns=&domain=&timeframe=last_day&nbresults=0
#

import urllib2
import os
from xml.dom import minidom

PINGED = "ptsw-foafs.xml"
TIMEOUT = 10

class PTSW:
    
    def __init__(self):
        self.rest = "http://pingthesemanticweb.com/rest/?url="

    def ping(self, uri):
        try:
            uri = uri.replace(":", "%3A")
            import socket
            socket.setdefaulttimeout(TIMEOUT)
            response = urllib2.urlopen(self.rest+uri).read()
            #print response
            responseParsed = self.parseResponse(response)
            return (responseParsed['flerror'] == 0)
        except:
            return False

    def alreadyPinged(self, uri):
        #stats:
        # - minidom.parse(PINGED): 0m21.666s
        # - actual: 0m0.412s (bad case, not pinged) 
        
        if (os.path.exists(PINGED)):
            uri = 'url="'+uri+'"'
            for line in open(PINGED):
                if uri in line:
                    return True
            return False
        else:
            print 'ERROR: ' + PINGED + ' file not founded'
            return False

    def parseResponse(self, response):
        dom = minidom.parseString(response)
        responses = dom.getElementsByTagName('response')
        dict = {}
        for node in responses[0].childNodes:
            if (not node.nodeType == node.TEXT_NODE):
                key = node.nodeName
                try:
                    value = int(node.firstChild.data)
                except:
                    value = node.firstChild.data
                dict[key] = value
                    
        return dict

    def parsePinged(self, pinged):
        uris = []
        dom = minidom.parse(pinged)
        docs = dom.getElementsByTagName('rdfdocument')
        for doc in docs:
            uris.append(doc.getAttribute('url'))
            
        return uris
        
            
        