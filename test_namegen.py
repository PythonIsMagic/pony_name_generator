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


def test_pluralize_noun_mouse():
    result = namegen.pluralize_noun('mouse')
    assert result == 'mice'


def test_pluralize_noun_roof():
    result = namegen.pluralize_noun('roof')
    assert result == 'roofs'


def test_pluralize_noun_belief():
    result = namegen.pluralize_noun('belief')
    assert result == 'beliefs'


def test_pluralize_noun_chef():
    result = namegen.pluralize_noun('chef')
    assert result == 'chefs'


def test_pluralize_noun_chief():
    result = namegen.pluralize_noun('chief')
    assert result == 'chiefs'


def test_pluralize_noun_gas():
    result = namegen.pluralize_noun('gas')
    assert result == 'gasses'


def test_pluralize_noun_fez():
    result = namegen.pluralize_noun('fez')
    assert result == 'fezzes'


def test_pluralize_noun_photo():
    result = namegen.pluralize_noun('photo')
    assert result == 'photos'


def test_pluralize_noun_piano():
    result = namegen.pluralize_noun('piano')
    assert result == 'pianos'


def test_pluralize_noun_halo():
    result = namegen.pluralize_noun('halo')
    assert result == 'halos'


def test_pluralize_noun_tooth():
    result = namegen.pluralize_noun('tooth')
    assert result == 'teeth'


# Tests for def rhyme(inp, level):
# Tests for def is_ryhme(word1, word2):
# Tests for def find_rhyme(word):

# Meh - don't care so much about testing these...
# def get_name(word_dict):
# def scan_files(prefix):
# def import_words():
