#/bin/bash

mypy src

flake8 src

tox

python3 -m twine upload dist/* --verbose