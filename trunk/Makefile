
DESTDIR =
PYTHON = python2.4

clean:
	rm -f `find . -name "*~"`
	rm -f `find . -name "*pyc"`
	rm -f `find . -name "*.bak"`
	rm -f data/*.data data/*.eps

tests:
	$(PYTHON) test/testfoaf.py
	$(PYTHON) test/testPySQLite.py
	$(PYTHON) test/testPTSW.py
	$(PYTHON) test/testFutilTracker.py
	$(PYTHON) test/testClientView.py
	$(PYTHON) test/testShaManager.py

stats:
	scripts/pool.sh
