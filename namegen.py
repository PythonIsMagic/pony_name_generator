""" namegen.py
    Generates random and interesting pony names.
"""

import argparse
import os
import random
DATA_DIR = 'data'

categories = [
    ('nouns', 'nouns'),
    ('nouns', 'verbs'),
    ('verbs', 'nouns'),
    ('adj', 'nouns'),
    ('adj', 'verbs'),
]


def get_name(word_dict):
    """ Creates a random name from a dictionary. """
    choice = random.choice(categories)
    # print(choice)
    words = [random.choice(word_dict[c]) for c in choice]
    return ' '.join(words)


def scan_files(prefix):
    """ Gets all words from all files ending in the specified prefix and returns
        them as a list.
    """
    files = ['/'.join([DATA_DIR, f]) for f in os.listdir("data") if f.startswith(prefix)]
    # Collect all the words from the files
    words = []
    for f in files:
        with open(f, 'r') as wf:
            for w in wf.readlines():
                if w:
                    words.append(w.strip().title())

    return list(set(words))


def import_words():
    """ Collects all the words from the data files.
        Creates a dictionary of nouns, verbs, and adjectives.
    """
    nouns = scan_files('nouns')  # Get nouns
    adjs = scan_files('adj')  # Get adjectives
    verbs = scan_files('verb')  # Get verbs

    # Create the dict
    word_dict = {}
    word_dict['nouns'] = nouns
    word_dict['adj'] = adjs
    word_dict['verbs'] = verbs
    return word_dict


def setup_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('qty', type=int,
                        help="The number of pony names to generate.")
    return parser


def main():
    """ Main run loop """
    print("Welcome to Erik's Pony Name Generator!")
    parser = setup_parser()
    args = parser.parse_args()

    word_dict = import_words()
    x = 0
    while x < args.qty:
        name = get_name(word_dict)
        print(name)
        x += 1


if __name__ == "__main__":
    main()
