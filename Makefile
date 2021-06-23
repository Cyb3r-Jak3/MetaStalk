PHONY: lint test check-dist

lint:
	black --check ./MetaStalk/
	pylint --rcfile=tox.ini ./MetaStalk/
	flake8 ./MetaStalk/
	bandit -r ./MetaStalk/

test:
	coverage run --source=./MetaStalk/ --append -m unittest -vv

check-dist:
	python setup.py egg_info
	python setup.py sdist bdist_wheel
	twine check dist/*