# Coding Challenges

[![CircleCI](https://img.shields.io/circleci/project/github/suddi/coding-challenges.svg)](https://circleci.com/gh/suddi/coding-challenges)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f49da84091a24ef8bae87bdc4ed10423)](https://www.codacy.com/app/Suddi/coding-challenges)
[![Greenkeeper badge](https://badges.greenkeeper.io/suddi/coding-challenges.svg)](https://greenkeeper.io/)
[![David](https://img.shields.io/david/suddi/coding-challenges.svg)](https://david-dm.org/suddi/coding-challenges)
[![David](https://img.shields.io/david/dev/suddi/coding-challenges.svg)](https://david-dm.org/suddi/coding-challenges?type=dev)
[![license](https://img.shields.io/github/license/suddi/coding-challenges.svg)](https://github.com/suddi/coding-challenges/blob/master/LICENSE)

Solutions to common coding challenge questions answered in Python 3.8, Node.js 12 and C++ 11.

## Setup

````sh
# Using virtualenvwrapper to manage virtual environments
pip install virtualenvwrapper
````

````sh
mkvirtualenv coding-challenges

# Install dependencies for Python
pip install --requirement requirements.txt --requirement test_requirements.txt

# Install dependencies for Node.js
npm install
````

## Lint

````sh
# Lint Python code with Pylint
python setup.py lint

# Lint Node.js code with Eslint
npm run lint
````

## Test

````sh
# Run Python doctests with Pytest
python setup.py test

# Run Node.js doctests with Mocha and jsdoctest
npm test

# Run C++ doctests with doctest.h at c++/doctest.h
node cpp_runner.js
````
