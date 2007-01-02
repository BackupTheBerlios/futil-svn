#!/usr/bin/env python2.4
# -*- coding: utf8 -*-

import sys
sys.path.append('./src')
from futil.storage.pySQLiteWrapper import PySQLiteWrapper

if __name__ == '__main__':
    if ( not len(sys.argv) == 2 ):
        print "Usage: ./createdb filename"
        sys.exit(-1)
    else:
        PySQLiteWrapper(sys.argv[1])
        
    
    
