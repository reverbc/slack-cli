venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

install:
	pip3 install . --editable

pipsi:
	pipsi install . --editable
