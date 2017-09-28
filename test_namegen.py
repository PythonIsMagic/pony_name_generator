import namegen


# Tests for def pluralize_noun(n):
def test_pluralize_noun_bat():
    result = namegen.pluralize_noun('bat')
    assert result == 'bats'


def test_pluralize_noun_sky():
    result = namegen.pluralize_noun('sky')
    assert result == 'skies'


def test_pluralize_noun_deer():
    result = namegen.pluralize_noun('deer')
    assert result == 'deer'


def test_pluralize_noun_mice():
    result = namegen.pluralize_noun('mice')
    assert result == 'mice'


# Tests for def rhyme(inp, level):
# Tests for def is_ryhme(word1, word2):
# Tests for def find_rhyme(word):

# Meh - don't care so much about testing these...
# def get_name(word_dict):
# def scan_files(prefix):
# def import_words():
