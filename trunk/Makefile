
DESTDIR =
PYTHON = python2.4

clean:
	rm -f *.pyc *~ *.bak

tests:
	$(PYTHON) testfoaf.py
	$(PYTHON) testPySQLite.py
	wget "http://pingthesemanticweb.com/export/?type=foaf&serialization=xml&timeframe=any_time&nbresults=0" --output-document=ptsw-foafs.xml
	$(PYTHON) testPTSW.py
	rm ptsw-foafs.xml
	$(PYTHON) testClientView.py
