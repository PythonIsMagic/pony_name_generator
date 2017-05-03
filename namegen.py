""" namegen.py
    Generates random and interesting pony names.
"""
import os
DATA_DIR = 'data'


def get_name(word_dict):
    """ Creates a random name from a dictionary. """


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
                    words.append(w.strip())

    return set(words)


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
    word_dict['adjs'] = adjs
    word_dict['verbs'] = verbs
    return word_dict


def main():
    """ Main run loop """
    print("Welcome to Erik's Pony Name Generator!")
    word_dict = import_words()


if __name__ == "__main__":
    main()
