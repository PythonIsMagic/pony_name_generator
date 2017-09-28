""" Module for having fun with rhymes. """
import nltk

"""
Resource u'corpora/cmudict' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/home/lunatunez/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'
"""


def rhyme(src_word, level):
    """
    level 0: Much stricter: 'bat' only matches {u'bat', u'batt', u'batte', u'bhatt'}
    level 1: Seems pretty open... 'bat' matches a LOT of weird stuff
    level 2: Seems more accurate
    """
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == src_word]
    rhymes = []
    for (word, syllable) in syllables:
            rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
    return set(rhymes)


def is_rhyme(word1, word2):
    # first, we don't want to report 'glue' and 'unglue' as rhyming words
    # those kind of rhymes are LAME
    if word1.find(word2) == len(word1) - len(word2):
        return False
    if word2.find(word1) == len(word2) - len(word1):
        return False

    return word1 in rhyme(word2, 2)


def find_rhyme(word):
    """ Finds a word that rhyhms with the given word."""
