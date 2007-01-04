#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')

from futil.tracker.ptswtracker import PTSWTracker
from futil.utils.ptsw import PTSW

if __name__ == '__main__':
    
    tracker = PTSWTracker('data/ptsw.db')
    ptsw = PTSW()
    
    while tracker.moreUrisToExplore():
        uri = tracker.getNextUri()
        ptsw.ping(uri)

