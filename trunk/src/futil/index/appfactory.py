from factoryPattern import Factory

from PyLucene import FSDirectory

from searchAppService import SearchAppService
from indexAppService import IndexAppService
from futil.storage.shaManager import ShaManager

import os

INDEX_DIR = "index"

d = FSDirectory.getDirectory(INDEX_DIR, not os.path.exists(INDEX_DIR))
s = ShaManager()

appServiceFactory = Factory()
appServiceFactory.register("createSearchService", SearchAppService, d, s)
appServiceFactory.register("createIndexService", IndexAppService, d, s)
