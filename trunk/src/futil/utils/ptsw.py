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
from futil.utils.logger import FutilLogger

TIMEOUT = 10

class PTSW:
    
    def __init__(self):
        self.rest = "http://pingthesemanticweb.com/rest/?url="
        self.pinged = 0
        self.log = FutilLogger()

    def ping(self, uri):
        try:
            import socket
            socket.setdefaulttimeout(TIMEOUT)
            response = urllib2.urlopen(self.rest + uri.replace(":", "%3A")).read()
            #print response
            responseParsed = self.parseResponse(response)
            ok = (responseParsed['flerror'] == 0)
            if ok:
                self.pinged += 1
                self.log.info(uri+' pinged')
            return ok
        except:
            self.log.error('problem pinging ' + uri)
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
        self.log.info(str(len(uris))+' parsed from ' + pinged)
        return uris
    
    def stats(self):
        return str(self.pinged) + ' URIs pinged'
    
    def __del__(self):
        self.log.info(self.stats())
        
            
        