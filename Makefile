install:
	pip install -r requirements.txt

test:
	python -m unittest test_app.py

run:
	python app.py
