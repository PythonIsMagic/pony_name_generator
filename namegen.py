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
    ['compound'],
    ['noun'],
    ['noun', 'noun'],
    ['noun', 'noun_plural'],
    ['noun', 'verb'],
    ['noun', 'verb_er'],

    ['verb_ing', 'noun'],
    ['verb_ing', 'noun_plural'],

    ['adj'],
    ['adj', 'noun'],
    ['adj', 'noun_plural'],
    ['adj', 'verb'],
    ['adj', 'verb_ing'],
    ['adj', 'verb_er'],

    # Adding random 3-letter-partials
    # ['verb', '3letter', 'noun'],
    # ['3letter', 'verb', 'noun'],

    # Suffix/prefix
    # ('suffix_noun', 'noun', 'noun'),
    # ('noun', 'suffix_noun', 'noun'),
    # ('suffix_noun', 'noun', 'verb'),
    # ('noun', 'suffix_verb', 'verb'),
    # ('suffix_verb', 'verb', 'noun'),
    # ('adj', 'suffix_noun', 'noun'),
    # ('adj', 'suffix_verb', 'verb'),

    # Rhymes
    # ('noun', 'rhyme'),
    # ('verb', 'rhyme'),

    # Alliterations
    ['noun', 'alliterate noun'],
    ['noun', 'alliterate noun_plural'],
    ['noun', 'alliterate verb'],
    ['noun', 'alliterate verb_er'],

    ['verb_ing', 'alliterate noun'],
    ['verb_ing', 'alliterate noun_plural'],

    ['adj', 'alliterate noun'],
    ['adj', 'alliterate noun_plural'],
    ['adj', 'alliterate verb'],
    ['adj', 'alliterate verb_ing'],
    ['adj', 'alliterate verb_er'],
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


def finish_name(parts):
    # bug - a single quote resets the length of the name, and capitalizes the
    # letter after the '
    # ie: bird's -> Bird'S

    return ' '.join(parts).title()


def get_name(word_dict, args):
    """ Creates a random name from a word dictionary. """

    choice = random.choice(formats)[:]

    if args.honorifics:
        choice.insert(0, 'honorific')

    parts = []

    for c in choice:
        word = None
        tries = 0
        while word is None and tries < 5:
            tries += 1

            if word_dict.get(c, None):
                word = random.choice(word_dict[c])

            elif c == 'rhyme':
                word = rhyme(parts[-1])  # Rhyme the last word
            elif c.startswith('alliterate'):
                part = c.split()[-1]
                word = alliteration(word_dict[part], parts[-1])  # Alliterate the last word)

            # Fallback is to show what category it is
            if not word:
                word = '#{}#'.format(c)

            # Check for repetition
            if len(parts) > 0 and word in parts[-1]:
                word = None
            else:
                break

        else:
            word = "Gnarfsplat"

        parts.append(word)

    return finish_name(parts)


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
    word_dict = {c: scan_files(c) for c in categories}

    # Transformations
    word_dict['verb_ing'] = [tr.to_ing_tense(v) for v in word_dict['verb']]
    word_dict['verb_er'] = [tr.verb_to_noun(v) for v in word_dict['verb']]
    word_dict['noun_plural'] = [tr.pluralize_noun(n) for n in word_dict['noun'] if n not in word_dict['noun_abstract']]

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
