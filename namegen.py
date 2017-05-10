""" namegen.py
    Generates random and interesting pony names.
"""

import argparse
import nltk
import os
import random
import sys
DATA_DIR = 'data'

categories = [
    ('nouns', None, 'nouns'),
    ('nouns', None, 'verbs'),
    ('verbs', None, 'nouns'),
    ('adj', None, 'nouns'),
    ('adj', None, 'verbs'),
    ('verbs', '3letter', None, 'nouns'),
    ('nouns', None, 'rhyme'),
    ('verbs', None, 'rhyme'),
]

class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def setup_parser():
    """ The parser should either take an integer or the -i arg.
    """
    parser = argparse.ArgumentParser(description="Generate some pony names!")

    parser.add_argument('-n', '--number', type=int,
                        help="The number of pony names to generate.")

    parser.add_argument('-i', '--interactive', action='store_true',
                        help="Use the name generator to interactively save or blacklist names.")
    return parser


def pluralize_noun(n):
    """ Takes a noun and turns it into it's plural form """

    if n.endswith('us'):
        return n[:-2] + 'i'
    elif n.endswith('is'):
        return n[:-2] + 'es'
    elif n.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z', 'o')):
        return n + 'es'
    elif n.endswith('f'):
        return n[:-1] + 'ves'
    elif n.endswith('fe'):
        return n[:-2] + 'ves'
    elif n.endswith('tion'):
        return n + 's'
    elif n.endswith('on'):
        return n[:-2] + 'a'
    elif n.endswith('y') and n[-2] in 'bcdfghjklmnpqrstvwxz':
        return n[:-1] + 'ies'
    else:
        return n + 's'


def rhyme(inp, level):
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == inp]
    rhymes = []
    for (word, syllable) in syllables:
            rhymes += [word for word, pron in entries if pron[-level:] == syllable[-level:]]
    return set(rhymes)


def is_ryhme(word1, word2):
    # first, we don't want to report 'glue' and 'unglue' as rhyming words
    # those kind of rhymes are LAME
    if word1.find(word2) == len(word1) - len(word2):
        return False
    if word2.find(word1) == len(word2) - len(word1):
        return False

    return word1 in rhyme(word2, 1)


def find_rhyme(word):
    """ Finds a word that rhyhms with the given word."""


def get_name(word_dict):
    """ Creates a random name from a dictionary. """
    choice = random.choice(categories)
    words = []
    for c in choice:
        if c:
            word = random.choice(word_dict[c])
            if c == 'nouns':
                # 2 in 5 chance it's plural
                if word not in word_dict['abstract_nouns'] and random.randint(1, 5) <= 2:
                    word = pluralize_noun(word)
            elif c == 'verbs':
                pass
                # Example: walk
                # 1 in 10 chance it's simple present tense: walk
                # 1 in 10 chance it's present tense: walks
                # 1 in 10 chance it's present continuous: walking
                # 1 in 10 chance it's past perfect tense: walked
            elif c == 'rhyme':
                word = find_rhyme(words[0])

            words.append(word)
        else:
            words.append(' ')
    return ''.join(words).title()


def scan_files(prefix):
    """ Gets all words from all files ending in the specified prefix and returns
        them as a list.
    """
    files = ['/'.join([DATA_DIR, f]) for f in os.listdir(DATA_DIR) if f.startswith(prefix)]

    words = []
    for f in files:
        # print('Scanning {}'.format(f))
        with open(f, 'r') as wf:
            for w in wf.readlines():
                if w:
                    words.append(w.strip())

    return list(set(words))


def import_words():
    """ Collects all the words from the data files.
        Creates a dictionary of nouns, verbs, and adjectives.
    """
    nouns = scan_files('nouns')
    abstract_nouns = scan_files('nouns_abstract')
    adjs = scan_files('adj')
    verbs = scan_files('verb')
    words3letter = scan_files('3letter')

    word_dict = {}
    word_dict['abstract_nouns'] = abstract_nouns
    word_dict['nouns'] = nouns
    word_dict['adj'] = adjs
    word_dict['verbs'] = verbs
    word_dict['3letter'] = words3letter
    return word_dict


def main():
    """ Main run loop """
    parser = setup_parser()
    args = parser.parse_args()
    word_dict = import_words()

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    elif args.number:
        for i in range(args.number):
            name = get_name(word_dict)
            print(name)

        exit()

    elif args.interactive:
        while True:
            name = get_name(word_dict)
            print(name)
            raw_input()


if __name__ == "__main__":
    main()
