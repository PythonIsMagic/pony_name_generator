# Project Name: namegen
> Generates random pony names.


## What's it?

[Project summary]
Fun project inspired by My Little Pony to generate random pony names.  Uses a database of
nouns, verbs, and adjectives and combines them in random ways to create entertaining names.

Also performs transformations on words to come up with the maximum variety possible.

Verbs are originally basic present tense but can be transformed as:
	simple present tense -> present continuous  (ie: 'walk' -> 'walking')
	simple present tense -> noun (ie: 'walk' -> 'walker')

Nouns are originally singular, but can be transformed as follows:
	singular noun -> plural noun (ie: 'box' -> 'boxes')

![](screenshot.png)

### Features
- **Interactive** Interactive One-by-one name generation
- **Bulk generation** Generate a list of any number of names 
- **Favoring** Mark your favorate names for later!
---

### Prerequisities
Python 2

#### Uses
* argparse, logging, pytest, nltk


## Usage
```
Interactive:
$ python namegen.py -i
```
For help: python main.py -h

***EXAMPLES:***
> Generate 10 names:
```
$ python namegen.py -n 10
```

> Generate 10 names with honorifics:
```
$ python namegen.py -h -n 10
```

---

### TODO

- [X] Fill in README details.
- [X] First commit: README
- [X] First branch:
- [ ] Add a screenshot to the README
- [ ] Configure konch to be really sexy with iPython
- [ ] Generate requirements.txt with $ pip freeze --local > requirements.txt
- [X] Thin out the music terminology a bit
- [ ] Make sure all official pony names are capable of being generated
- [ ] Blacklist all official pony names - we want originals!
- [X] Don't repeat similar words in a single name ('Walking Walker')
- [ ] Fix: Some nouns are getting cut off "Ica" "Moa"
- [ ] Single word names - Maybe limit to over 2 syllables
- [ ] Count syllables in a word (NLTK?)
- [X] Add alliteration
- [X] When creating the database, add all variations from the start
- [ ] Add support for a persistant shelve database, updating, etc.
- [X] Make the combos better
- [X] Make honorifics optional from command line
- [ ] noun transformations
- [X] Add verb past tense transformations
- [ ] Create a Django site - one page, to handle generating names
- [ ] Create an IOS app
- [ ] Port to Android
---

## Meta
##### Author: Erik Lunna
##### Start Date: 2016-11-24
##### Twitter -- [@ ](https://twitter.com/ )
##### Email -- eslunna@gmail.com

[![](http://img.shields.io/badge/license-WTFPL-blue.svg)]
[WTFPL]: See ``LICENSE`` for full text.
