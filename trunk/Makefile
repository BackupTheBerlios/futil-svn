
DESTDIR =
PYTHON = python2.4

clean:
	rm -f `find . -name "*~"`
	rm -f `find . -name "*pyc"`
	rm -f `find . -name "*.bak"`
	rm -f `find . -name "semantic.cache"`
	rm -f data/*.data data/*.eps
	rm -rf doc/epydoc

epydoc:
	mkdir -p doc/epydoc
	epydoc -n futil -o doc/epydoc/ --html src/futil/
tests:
	$(PYTHON) test/testfoaf.py
	$(PYTHON) test/testPySQLite.py
	$(PYTHON) test/testPTSW.py
	$(PYTHON) test/testFutilTracker.py
	$(PYTHON) test/testClientView.py
	$(PYTHON) test/testShaManager.py

test-foaf:
	$(PYTHON) test/testFriendsFilter.py
	$(PYTHON) test/testGeoposFilter.py
	$(PYTHON) test/testNameFilter.py
	$(PYTHON) test/testNickFilter.py
	$(PYTHON) test/testShaFilter.py
	$(PYTHON) test/testFoaf.py

stats:
	scripts/pool.sh
	scripts/popularSites.sh
	scripts/popular.sh
