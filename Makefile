install:
	python setup.py install

clean:
	rm -rf *.pyc

upload:
	python setup.py register sdist upload

doc: cog

cog:
	cd runwrf && cog.py -r __init__.py

test:
	echo "No tests written yet"

.PHONY : test doc clean install
