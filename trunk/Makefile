
DESTDIR =
PYTHON = python2.4

clean:
	rm -f *.pyc *~ *.bak

tests:
	$(PYTHON) test/testfoaf.py
	$(PYTHON) test/testPySQLite.py
	#wget "http://pingthesemanticweb.com/export/?type=foaf&serialization=xml&timeframe=any_time&nbresults=0" --output-document=ptsw-foafs.xml
	$(PYTHON) test/testPTSW.py
	#rm ptsw-foafs.xml
	$(PYTHON) test/testClientView.py
