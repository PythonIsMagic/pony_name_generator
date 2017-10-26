""" namegen.py
    Generates random and interesting pony names.
"""

import argparse
import os
import random
import plurals
import rhymes
import sys

DATA_DIR = 'data'

formats = [
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
    """ The parser should either take an integer or the -i arg. """

    parser = argparse.ArgumentParser(description='Generate some pony names!')

    parser.add_argument('-n', '--number', type=int,
                        help='The number of pony names to generate.')

    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Use the name generator to interactively save or blacklist names.')
    return parser


def get_name(word_dict):
    """ Creates a random name from a word dictionary. """

    choice = random.choice(formats)
    words = []

    for c in choice:
        if c:
            word = random.choice(word_dict[c])

            if c == 'nouns':
                word = process_noun(word_dict, word)
            elif c == 'verbs':
                word = process_verb(word_dict, word)
            elif c == 'rhyme':
                word = process_rhyme(word_dict, words[0])

            # Fallback is to just pick something else random...
            if not word:
                word = random.choice(word_dict[choice[0]])

            words.append(word)

        else:
            # If c is None - append a space to the name
            words.append(' ')

    return ''.join(words).title()


def process_noun(word_dict, word):
    # 1 in 10 chance it's plural
    if word not in word_dict['abstract_nouns'] and random.randint(1, 10) <= 1:
        return plurals.pluralize_noun(word)
    else:
        return word


def process_verb(word_dict, word):
    pass
    # Example: walk
    # 1 in 10 chance it's simple present tense: walk
    # 1 in 10 chance it's present tense: walks
    # 1 in 10 chance it's present continuous: walking
    # 1 in 10 chance it's past perfect tense: walked


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
    word_dict['rhyme'] = ['']
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
