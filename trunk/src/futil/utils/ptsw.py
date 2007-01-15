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

import urllib, urllib2
import os
from xml.dom import minidom
from futil.utils.logger import FutilLogger
from ConfigParser import ConfigParser

TIMEOUT = 10

class PTSW:
    
    def __init__(self, app='futil', config='.ptsw'):
        self.rest = "http://pingthesemanticweb.com/rest/?url="
        self.log = FutilLogger(app)
        self.stats = {'pinged':0, 'sioc':0, 'foaf':0, 'doap':0, 'owl':0, 'rdfs':0, 'rdf':0, 'flerror':0}
        self.pathStats = config
        self.loadStats()

    def ping(self, uri):
        try:
            import socket
            socket.setdefaulttimeout(TIMEOUT)
            
            #TODO: 
            # proxy: urllib2.ProxyHandler({})
            
            url = self.rest + urllib.quote(uri)
            data = {}
            headers = { 'User-Agent' : 'futil' }
            request = urllib2.Request(url, data, headers)
            response = urllib2.urlopen(request).read() #don't works the ping with especial URLs
            responseParsed = self.parseResponse(response)
            
            ok = (responseParsed['flerror'] == 0)
            self.setStats(responseParsed)
            if ok:
                self.stats['pinged'] += 1
                self.log.info(uri+' pinged')
            else:
                self.log.error('error pinging ' + uri + ': ' + responseParsed['message'])
            return ok
        except Exception, details:
            print str(details)
            self.log.error('problem pinging ' + uri + ': ' + str(details))
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
        try:
            dom = minidom.parse(pinged)
        except:
            self.log.error('problem parsing ' + pingued)
        docs = dom.getElementsByTagName('rdfdocument')
        for doc in docs:
            uris.append(doc.getAttribute('url'))
        self.log.info(str(len(uris))+' parsed from ' + pinged)
        return uris
    
    def loadStats(self):
        if(os.path.exists(self.pathStats)):
            config = ConfigParser()
            try:
                config.read(self.pathStats)
                section = 'PTSW'    
                
                if (config.has_section(section)):
                    for key in config.options(section):
                        if self.stats.has_key(key):
                            try:
                                value = int(config.get(section, key))
                            except:
                                value = 0
                            self.stats[key] = value     
                else:
                    print 'no'           
            except:
                self.log.error('parsing PTSW config file')
        else:
            self.log.info('no PTSW stats file founded')
    
    def saveStats(self):
        section = 'PTSW'
        ini = ConfigParser()
        ini.add_section(section)

        for key in self.stats.keys():
            ini.set(section, key, str(self.stats[key]))
                     
        try:
            file = open(self.pathStats, 'w+')
            ini.write(file)
            file.flush()
            file.close()
            self.log.info('PTSW stats saved in ' + self.pathStats)
        except Exception, details:
            self.log.error('saving PTSW stats in ' + self.pathStats + ': ' + str(details)) 
    
    def setStats(self, new):
        for key in new.keys():
            if (key != 'message'):
                self.stats[key] += new[key]
    
    def printStats(self):
        print '\n'
        print 'PingTheSemanticWeb wrapper stats:'
        for key in self.stats.keys():
            if (key!='pinged' and key!='flerror'):
                print '\t- ' + key + ': ' + str(self.stats[key])
        print '\t- errors: ' + str(self.stats['flerror'])
        print '\t- TOTAL PINGED: ' + str(self.stats['pinged'])
        print '\n'
        return self.stats['pinged']
    
    def close(self):
        self.log.info(str(self.stats['pinged']) + ' pinged')
        self.saveStats()
        self.printStats()
    
