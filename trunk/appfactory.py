from factoryPattern import Factory

from PyLucene import FSDirectory

from searchAppService import SearchAppService
from indexAppService import IndexAppService

import os

INDEX_DIR = "/tmp/borrame"

d = FSDirectory.getDirectory(INDEX_DIR, not os.path.exists(INDEX_DIR))

appServiceFactory = Factory()
appServiceFactory.register("createSearchService", SearchAppService, d)
appServiceFactory.register("createIndexService", IndexAppService, d)
