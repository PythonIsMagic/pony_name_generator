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

formats = [
    # ('compound',),
    ('noun', None, 'noun'),
    ('noun', None, 'verb'),
    ('verb', None, 'noun'),
    ('adj', None, 'noun'),
    ('adj', None, 'verb'),

    ('verb', '3letter', None, 'noun'),

    # ('suffix_noun', 'noun', None, 'noun'),
    # ('noun', None, 'suffix_noun', 'noun'),
    # ('suffix_noun', 'noun', None, 'verb'),
    # ('noun', None, 'suffix_verb', 'verb'),
    # ('suffix_verb', 'verb', None, 'noun'),
    # ('adj', None, 'suffix_noun', 'noun'),
    # ('adj', None, 'suffix_verb', 'verb'),

    # ('nouns', None, 'rhyme'),
    # ('verbs', None, 'rhyme'),

    ('honorific', None, 'compound',),
    ('honorific', None, 'noun', None, 'noun'),
    ('honorific', None, 'noun', None, 'verb'),
    ('honorific', None, 'verb', None, 'noun'),
    ('honorific', None, 'adj', None, 'noun'),
    ('honorific', None, 'adj', None, 'verb'),
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
                        help='Use the name generator to interactively save or blacklist names.')

    parser.add_argument('-r', '--review', action='store_true',
                        help='Check all the word entries that are being used.')
    return parser


def get_name(word_dict):
    """ Creates a random name from a word dictionary. """

    choice = random.choice(formats)
    words = []

    for c in choice:
        word = None

        if c is None:
            word = ' '  # Just adding a space
        elif word_dict.get(c, None):
            word = random.choice(word_dict[c])

            if c == 'nouns':
                word = process_noun(word_dict, word)
            elif c == 'verbs':
                word = process_verb(word_dict, word)
        elif c == 'rhyme':
            word = process_rhyme(word_dict, words[0])

        # Fallback is to just pick something else random...
        if not word:
            # word = random.choice(word_dict[choice[0]])
            word = '#{}#'.format(c)

        words.append(word)

    # 1 in 5 chance we do honorific!
    # if random.randint(1, 5) == 1:
        # words.insert(0, random.choice(word_dict['honorifics']) + ' ')

    name = ''.join(words).title()
    return '{:35} {}'.format(name, choice)


def process_noun(word_dict, word):
    if word in word_dict['nouns_abstract']:
        return word  # It's already plural...
    elif random.randint(1, 10) <= 1:
        # 1 in 10 chance it's plural
        return tr.pluralize_noun(word)
    else:
        return word


def process_verb(word_dict, word):
    n = random.randint(1, 10)
    if n == 1:
        # 1 in 10 chance it's present continuous: walking
        return tr.to_ing_tense(word)
    elif n == 2:
        # 1 in 10 chance it's a verb transformed into a noun
        return tr.verb_to_noun(word)
    else:
        # Otherwise just a normal verb
        return word


def process_rhyme(word_dict, word):
    print('\t*** Rhyming!')
    # We'll attempt to rhyme the first word
    return rhymes.find_rhyme(word)


def scan_files(prefix):
    """ Gets all words from all files ending in the specified prefix and returns
        them as a list.
    """
    files = ['/'.join([DATA_DIR, f]) for f in os.listdir(DATA_DIR) if f.startswith(prefix)]

    words = []
    for f in files:
        with open(f, 'r') as wf:
            for w in wf.readlines():
                if w:
                    words.append(w.strip())

    return list(set(words))


def import_words():
    """ Collects all the words from the data files.
        Creates a dictionary of nouns, verbs, and adjectives.
    """
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
    return {c: scan_files(c) for c in categories}


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
            name = get_name(word_dict)
            print(name)

    elif args.interactive:
        while True:
            name = get_name(word_dict)
            print(name)
            raw_input()

    sys.exit(1)

if __name__ == "__main__":
    main()
