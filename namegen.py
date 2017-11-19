""" namegen.py
    Generates random and interesting pony names.
"""

import argparse
import os
import random
import plurals
import rhymes
import sys
import tenses

DATA_DIR = 'data'

formats = [
    # ('compound_names',),
    ('nouns', None, 'nouns'),
    ('nouns', None, 'verbs'),
    ('verbs', None, 'nouns'),
    ('adj', None, 'nouns'),
    ('adj', None, 'verbs'),

    # ('verbs', '3letter', None, 'nouns'),

    # ('suffix_noun', 'nouns', None, 'nouns'),
    # ('nouns', None, 'suffix_noun', 'nouns'),
    # ('suffix_noun', 'nouns', None, 'verbs'),
    # ('nouns', None, 'suffix_verb', 'verbs'),
    # ('suffix_verb', 'verbs', None, 'nouns'),
    # ('adj', None, 'suffix_noun', 'nouns'),
    # ('adj', None, 'suffix_verb', 'verbs'),

    # ('nouns', None, 'rhyme'),
    # ('verbs', None, 'rhyme'),

    # ('honorifics', None, 'compound_names',),
    # ('honorifics', None, 'nouns', None, 'nouns'),
    # ('honorifics', None, 'nouns', None, 'verbs'),
    # ('honorifics', None, 'verbs', None, 'nouns'),
    # ('honorifics', None, 'adj', None, 'nouns'),
    # ('honorifics', None, 'adj', None, 'verbs'),
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
        return plurals.pluralize_noun(word)
    else:
        return word


def process_verb(word_dict, word):
    n = random.randint(1, 10)
    if n == 1:
        # 1 in 10 chance it's present continuous: walking
        return tenses.to_ing_tense(word)
    elif n == 2:
        # 1 in 10 chance it's a verb transformed into a noun
        return tenses.verb_to_noun(word)
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
        'nouns',
        'nouns_abstract',
        'verbs',
        # 'rhyme',
        'honorifics',
        'suffix',
        'compound_names',
        'suffix_noun',
        'suffix_verb',
    )
    return {c: scan_files(c) for c in categories}


def review_word_dict(word_dict):
    print('Reviewing word_dict')
    for k, v in word_dict.items():
        print('Category: {} has {} entries.'.format(k, len(v)))


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
