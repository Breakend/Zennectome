install:
	apt-get install -y libigraph0-dev
	python setup.py install
test:
	python setup.py test	
