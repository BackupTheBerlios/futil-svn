
DESTDIR =
PYTHON = python2.4

clean:
	rm -f `find . -name "*~"`
	rm -f `find . -name "*pyc"`
	rm -f `find . -name "*.bak"`

tests:
	$(PYTHON) test/testfoaf.py
	$(PYTHON) test/testPySQLite.py
	#wget "http://pingthesemanticweb.com/export/?type=foaf&serialization=xml&timeframe=any_time&nbresults=0" --output-document=ptsw-foafs.xml
	$(PYTHON) test/testPTSW.py
	#rm ptsw-foafs.xml
	$(PYTHON) test/testClientView.py
	$(PYTHON) test/testShaManager.py
	