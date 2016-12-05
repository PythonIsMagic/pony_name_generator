#!/usr/bin/env python3

import random


def line():
    print('#######################################################')


def readfile(filename):
    """Read all the lines from a file into a list and return the list"""
    newlist = []
    with open(filename, 'r') as f:
        for line in f:
            newlist.append(line.strip())
    return newlist


def verb_noun():
    return '{} {}'.format(random.choice(VERBS), random.choice(NOUNS))


# Pattern: Shutterfly
def verb_emotion():
    return '{}{}'.format(random.choice(VERBS), random.choice(THREELETTERS))


def adj_noun():
    return '{} {}'.format(random.choice(ADJ), random.choice(NOUNS))


def adj_verb():
    return '{} {}'.format(random.choice(ADJ), random.choice(VERBS))


# Pattern: Rainbow Dash
def noun_verb():
    return '{} {}'.format(random.choice(NOUNS), random.choice(VERBS))


# Pattern: Rainbow Dash/Alternative
def light_verb():
    return '{} {}'.format(random.choice(LIGHTS), random.choice(VERBS))


# Pattern: Twilight Sparkle
def light_light():
    return '{} {}'.format(random.choice(LIGHTS), random.choice(LIGHTS))


# Sunset Shimmer, Starlight Glimmer, etc
def nounverb_light():
    return '{}{} {}'.format(random.choice(VERBS), random.choice(NOUNS), random.choice(LIGHTS))


def format_name(name):
    name = name.lower().split()
    name = [n.capitalize() for n in name]
    return ' '.join(name)


#  EMOTIONS = readfile('emotions.txt')
NOUNS = readfile('nouns.txt')
LIGHTS = readfile('lights.txt')
VERBS = readfile('verbs.txt')
THREELETTERS = readfile('3letterwords.txt')
ADJ = readfile('adjectives.txt')


while True:
    print(format_name(verb_noun()))
    print(format_name(verb_emotion()))
    print(format_name(adj_noun()))
    print(format_name(adj_verb()))
    print(format_name(noun_verb()))
    print(format_name(light_verb()))
    print(format_name(light_light()))
    print(format_name(nounverb_light()))
    input('>')
