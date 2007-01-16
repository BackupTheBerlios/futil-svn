#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

from futil.crawler.crawler import Crawler
from futil.tracker.ptswtracker import PTSWTracker
from futil.index.appfactory import appServiceFactory

import signal

if __name__ == "__main__":
    
    tracker = PTSWTracker(pinged='data/initial.xml')
    indexer = appServiceFactory.createIndexService()
    crawler = Crawler(tracker, indexer)  #FIXME

    def finale(a, b):
        crawler.finish()
        sys.exit(0)

    signal.signal(signal.SIGHUP, finale)
    crawler.start()