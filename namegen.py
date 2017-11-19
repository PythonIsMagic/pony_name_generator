""" namegen.py
    Generates random and interesting pony names.
"""

import argparse
import os
import random
import rhymes
import sys
import transformations as tr

DATA_DIR = 'data'

categories = (
    '3letter',
    'adj',
    'noun',
    'noun_abstract',
    'verb',
    # 'rhyme',
    'honorific',
    'suffix',
    'compound',
    'suffix_noun',
    'suffix_verb',
)

formats = [
    # ('compound',),
    # ['noun', None, 'noun'],
    ['noun', None, 'alliterate noun'],
    ['noun', None, 'alliterate verb'],
    ['noun', None, 'alliterate adj'],
    # ['noun', None, 'noun_plural'],

    # ['noun', None, 'verb'],
    # ['noun', None, 'verb_er'],
    # ['verb', None, 'noun'],
    # ['verb_ing', None, 'noun'],

    # ['adj', None, 'noun'],
    # ['adj', None, 'noun_plural'],
    # ['adj', None, 'verb'],
    # ['adj', None, 'verb_ing'],
    # ['adj', None, 'verb_er'],

    # Adding random 3-letter-partials
    # ['verb', '3letter', None, 'noun'],
    # ['3letter', 'verb', None, 'noun'],

    # Suffix/prefix
    # ('suffix_noun', 'noun', None, 'noun'),
    # ('noun', None, 'suffix_noun', 'noun'),
    # ('suffix_noun', 'noun', None, 'verb'),
    # ('noun', None, 'suffix_verb', 'verb'),
    # ('suffix_verb', 'verb', None, 'noun'),
    # ('adj', None, 'suffix_noun', 'noun'),
    # ('adj', None, 'suffix_verb', 'verb'),

    # Rhymes
    # ('noun', None, 'rhyme'),
    # ('verb', None, 'rhyme'),

    # Alliterations
]


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def setup_parser():
    """ The parser should either take an integer or the -i arg. """

    parser = argparse.ArgumentParser(description='Generate some pony names!')

    parser.add_argument('-n', '--number', type=int,
                        help='The number of pony names to generate.')

    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Generate names one by one - interactively blacklist or like.')

    parser.add_argument('-r', '--review', action='store_true',
                        help='Check all the word entries that are being used.')

    parser.add_argument('-H', '--honorifics', action='store_true',
                        help='Adds an honorific prefix to each name.')

    return parser


def get_name(word_dict, args):
    """ Creates a random name from a word dictionary. """

    choice = random.choice(formats)[:]

    if args.honorifics:
        choice.insert(0, 'honorific')
        choice.insert(1, None)

    words = []

    for c in choice:
        word = None

        if c is None:
            word = ' '  # Just adding a space
        elif word_dict.get(c, None):
            word = random.choice(word_dict[c])

        elif c == 'rhyme':
            word = rhyme(words[-2])  # Rhyme the last word
        elif c.startswith('alliterate'):
            part = c.split()[-1]
            word = alliteration(word_dict[part], words[-2])  # Alliterate the last word)
        # Fallback is to show what category it is
        if not word:
            word = '#{}#'.format(c)

        words.append(word)

    name = ''.join(words).title()
    return '{:40} {}'.format(name, choice)


def rhyme(word):
    print('\t*** Rhyming!')
    # We'll attempt to rhyme the first word
    return rhymes.find_rhyme(word)


def alliteration(word_list, word):
    first_letter = word[0]
    possibilites = [w for w in word_list if w.startswith(first_letter)]

    if len(possibilites) > 0:
        return random.choice(possibilites)
    else:
        return random.choice(word_list)


def scan_files(prefix):
    """ Gets all words from all files ending in the specified prefix and returns
        them as a list.
    """
    files = ['/'.join([DATA_DIR, f]) for f in os.listdir(DATA_DIR) if f.startswith(prefix)]

    words = []
    for f in files:
        with open(f, 'r') as wf:
            for w in wf.readlines():
                w = w.strip()
                if w:
                    words.append(w)

    return list(set(words))


def import_words():
    """ Collects all the words from the data files.
        Creates a dictionary of nouns, verbs, and adjectives.
    """

    print('Importing database')
    word_dict = {c: scan_files(c) for c in categories}

    # Transformations
    print('Processing transformations!')
    word_dict['verb_ing'] = [tr.to_ing_tense(v) for v in word_dict['verb']]
    word_dict['verb_er'] = [tr.verb_to_noun(v) for v in word_dict['verb']]
    word_dict['noun_plural'] = [tr.pluralize_noun(n) for n in word_dict['noun'] if n not in word_dict['noun_abstract']]

    print('Import and transformations complete!')
    return word_dict


def review_word_dict(word_dict):
    print('Reviewing word_dict')
    allwords = [w for c in word_dict.values() for w in c]
    print('{} total words used'.format(len(allwords)))
    print('{} unique words used'.format(len(set(allwords))))

    for k, v in word_dict.items():
        print('Category: {} has {} entries.'.format(k, len(v)))

    dupes = sorted(list(set([w for w in allwords if allwords.count(w) > 1])))
    print('These words occur in more than one list')

    for d in dupes:
        print(d)


def main():
    """ Main run loop """
    parser = setup_parser()
    args = parser.parse_args()
    word_dict = import_words()

    if len(sys.argv) == 1:
        parser.print_help()
    elif args.review:
        review_word_dict(word_dict)
    elif args.number:
        for i in range(args.number):
            name = get_name(word_dict, args)
            print(name)

    elif args.interactive:
        while True:
            name = get_name(word_dict, args)
            print(name)
            raw_input()

    sys.exit(1)

if __name__ == "__main__":
    main()
