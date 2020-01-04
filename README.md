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

## Python Cheatsheet

### General

````py
# Swap numbers a, b
a = 3                                                               # O(1)
b = 2                                                               # O(1)
# a = 2, b = 3
a, b = b, a                                                         # O(1)

# Format print statements
# a = 2, b = 3
print("a = {0}, b = {1}".format(a, b))                              # O(1)

# False
all([3, 2, -1, 0])                                                  # O(N)

# True
any([3, 2, -1, 0])                                                  # O(N)

# '0b1000'
bin(8)                                                              # O(1)

# '0x58'
hex(88)                                                             # O(1)

# True
bool(-1)                                                            # O(1)

# '0'
chr(48)                                                             # O(1)
# 'A'
chr(65)                                                             # O(1)
# 'a'
chr(97)                                                             # O(1)
# 97
ord('a')                                                            # O(1)

# See all operations available
dir(list)                                                           # O(1)

# Get position and value during iteration
position, value = enumerate([3, 2, -1, 0])                          # O(N)

# Iterate through range
range(0, 5)                                                         # O(N)

# Take input from stdin
a = input('What is your name? ')                                    # O(1)

# True
isinstance([3, 2, 1], list)                                         # O(1)

# 'el'
'hello'[slice(1, 3, 1)]                                             # O(j - i)
````

### Functional Programming

````py
# [2, 4, 6]
list(map(lambda x: x * 2, [1, 2, 3]))                               # O(N)

# [5, 7, 9]
list(map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]))                 # O(N)

# [1, 3]
list(filter(lambda x: x % 2, [1, 2, 3]))                            # O(N)
````

### Math

````py
# Set to infinity
a = float('inf')                                                    # O(1)

# Set to negative infinity
a = float('-inf')                                                   # O(1)

# Raise to exponential power
# 8
2 ** 3                                                              # O(1)
# 8
pow(2, 3)                                                           # O(1)

# 32.3
abs(-32.3)                                                          # O(1)

# Returns a tuple containing the quotient and remainder
# (2, 2)
divmod(8, 3)                                                        # O(1)

# 4.22
round(4.222, 2)                                                     # O(1)

# 9
sum([3, 4, 2])                                                      # O(1)
````

### List Operations

````py
a = [5]                                                             # O(1)

# a = 5
a[0]                                                                # O(1)

# 1
len(a)                                                              # O(1)

# a = [5, 4]
a.append(4)                                                         # O(1)

b = [3, 2]                                                          # O(1)
# a = [5, 4, 3, 2]
a.extend(b)                                                         # O(len(b)) => O(N)

b = [1, 0]                                                          # O(1)
# [5, 4, 3, 2, 1, 0]
a + b                                                               # O(len(b)) => O(N)

# b = 2, a = [5, 4, 3]
b = a.pop()                                                         # O(1)

# a = []
a.clear()                                                           # O(1)

# a = [5, 4, 3, 2, 1, 0]
a = [5, 4, 3, 2, 1, 0]                                              # O(1)

# [3, 2]
a[2:4]                                                              # O(4 - 2) => O(j - i)

# b = [5, 4, 3, 2, 1, 0]
b = [5, 4, 3, 2, 1, 0]                                              # O(1)

# True
a == b                                                              # O(N)

# False
a != b                                                              # O(N)

# a = [6, 5, 4, 3, 2, 1, 0]
a.insert(0, 6)                                                      # O(N)

# a = [5, 4, 3, 2, 1, 0]
del a[0]                                                            # O(N)

# a = [5, 3, 2, 1, 0]
a.remove(4)                                                         # O(N)

v = 9                                                               # O(1)
# False
v in a                                                              # O(N)

# [5, 3, 2, 1, 0]
a.copy()                                                            # O(N)

# b = 5, a = [3, 2, 1, 0]
b = a.pop(0)                                                        # O(N)

# 0
min(a)                                                              # O(N)

# 3
max(a)                                                              # O(N)

# a = [0, 1, 2, 3]
a.reverse()                                                         # O(N)

# a = [0, 1, 2, 3], b = [0, 10, 20, 30]
b = []
for value in a:                                                     # O(N)
    b.append(value * 10)                                            # O(1)

# a = [0, 1, 2, 3], b = [0, 10, 20, 30]
b = map(lambda v: v * 10, a)                                        # O(N)

# a = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
a = 3 * a                                                           # O(3N) => O(kN)

# a = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3]
a.sort()                                                            # O(NlogN)

# a = [3, 3, 3, 2, 2, 2, 1, 1, 1, 0, 0, 0]
a.sort(reverse=True)                                                # O(NlogN)

# 9
a.index(0)                                                          # O(N)

# 3
a.count(1)                                                          # O(N)
````

### Dictionary Operations

````py
a = {'i': 4, 'j': 5, 'k': 6, 'l': 9, 'm': 2}                        # O(1)

# 4
a['i']                                                              # O(1)

# a = {'i': 1, 'j': 5, 'k': 6, 'l': 9, 'm': 2}
a['i'] = 1                                                          # O(1)

# 5
len(a)                                                              # O(1)

# a = {'j': 5, 'k': 6, 'l': 9, 'm': 2}
del a['i']                                                          # O(1)

# 10
a.get('i', 10)                                                      # O(1)

# a = {'j': 5, 'k': 6, 'l': 9, 'm': 2, 'i': 1}
a.setdefault('i', 1)                                                # O(1)

# 1, a = {'j': 5, 'k': 6, 'l': 9, 'm': 2}
a.pop('i')                                                          # O(1)

# ('m', 2), a = {'j': 5, 'k': 6, 'l': 9}
a.popitem()                                                         # O(1)

v = 9
# False
v in a                                                              # O(1)

# ['j', 'k', 'l']
a.keys()                                                            # O(1)

# [5, 6, 9]
a.values()                                                          # O(1)

# [('j', 5), ('k', 6), ('l', 9)]
a.items()                                                           # O(1)

# a = {}
a.clear()                                                           # O(1)

b = [('c', 1), ('d', 3)]
# a = {'c': 1, 'd': 3}
a = dict(b)                                                         # O(N)

# False
a == b                                                              # O(N)
# True
a == dict(b)                                                        # O(N)

# True
a != b                                                              # O(N)

# a = {'c': 12, 'd': 3}
a['c'] = 12                                                         # O(1)

# 'c'
min(a)                                                              # O(N)

# 'd'
max(a)                                                              # O(N)

b = ['a', 'e', 'i', 'o', 'u']                                       # O(1)
# a = {'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'vowel', 'u': 'vowel'}
a = a.fromkeys(b, 'vowel')                                          # O(N)

# {'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'vowel', 'u': 'vowel'}
a.copy()                                                            # O(N)

# {'a': 'vowel', 'e': 'vowel', 'i': 'vowel', 'o': 'meh', 'u': 'vowel', 'y': 'not-really-a-vowel'}
a.update({'y': 'not-really-a-vowel', 'o': 'meh'})                   # O(N)
````

# Tuple Operations

````py
a = (4, 5, 6, 9, 2)                                                 # O(1)

# 4
a[0]                                                                # O(1)

# 5
len(a)                                                              # O(1)

# [6, 9]
a[2:4]                                                              # O(4 - 2) => O(j - i)

b = [1, 3]                                                          # O(1)
# b = (1, 3)
tuple(b)                                                            # O(len(b)) => O(N)

# False
a == b                                                              # O(N)

# True
a != b                                                              # O(N)

v = 9                                                               # O(1)
# True
v in a                                                              # O(N)

# 2
min(a)                                                              # O(N)

# 9
max(a)                                                              # O(N)

b = []
# b = [8, 10, 12, 18, 4]
for v in a                                                          # O(N)
    b.append(a * 2)                                                 # O(1)

# (4, 5, 6, 9, 2, 4, 5, 6, 9, 2, 4, 5, 6, 9, 2)
3 * a                                                               # O(3N) => O(kN)

# 3
a.count(2)                                                          # O(N)

# 4
a.index(2)                                                          # O(N)
````

### Set Operations

````py
a = set([4, 5, 6, 9, 2, 4])                                         # O(1)

# 5
len(a)                                                              # O(1)

# a = {2, 4, 5, 6, 7, 9}
a.add(7)                                                            # O(1)

v = 9                                                               # O(1)
# True
v in a                                                              # O(1)

# a = {2, 4, 5, 7, 9}
a.remove(6)                                                         # O(1)

# a = {2, 4, 7, 9}
a.discard(5)                                                        # O(1)

# 2, a = {4, 7, 9}
a.pop()                                                             # O(1)

# a = {}
a.clear()                                                           # O(1)

b = [1, 1, 3]                                                       # O(1)
a = {1, 3}
a = set(b)                                                          # O(len(b)) => O(N)

b = {}                                                              # O(1)
# a = {1, 3}, b = {1, 2, 3, 6}
for v in a                                                          # O(N)
    b.add(a * 2)                                                    # O(1)

# False
a == b                                                              # O(N)

# True
a != b                                                              # O(N)

# True
a < b                                                               # O(N)

# True
a <= b                                                              # O(N)

# False
a > b                                                               # O(N)

# False
a >= b                                                              # O(N)

# {1, 2, 3, 6}
a | b                                                               # O(len(a) + len(b)) => O(M + N)

# {1, 3}
a & b                                                               # O(len(a) + len(b)) => O(M + N)

# {}
a - b                                                               # O(len(a) + len(b)) => O(M + N)

# {2, 6}
a ^ b                                                               # O(len(a) + len(b)) => O(M + N)

# {1, 3}
a.copy()                                                            # O(N)

# 1
min(a)                                                              # O(N)

# 3
max(a)                                                              # O(N)
````

### Object Operations

````py
class A():
    def __init__(self):                                             # O(1)
        self.a = 42                                                 # O(1)

v = A()                                                             # O(1)

# False
hasattr(v, 'b')                                                     # O(1)

# 42
getattr(v, 'a')                                                     # O(1)

# v.a = 42, v.b = 36
setattr(v, 'b', 36)                                                 # O(1)

# v.b = 36
delattr(v, 'a')                                                     # O(1)
````
