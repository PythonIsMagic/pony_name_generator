import plurals


# Tests for def pluralize_noun(n):
def test_pluralize_noun_bat():
    result = plurals.pluralize_noun('bat')
    assert result == 'bats'


def test_pluralize_noun_sky():
    result = plurals.pluralize_noun('sky')
    assert result == 'skies'


def test_pluralize_noun_deer():
    result = plurals.pluralize_noun('deer')
    assert result == 'deer'


def test_pluralize_noun_mouse():
    result = plurals.pluralize_noun('mouse')
    assert result == 'mice'


def test_pluralize_noun_roof():
    result = plurals.pluralize_noun('roof')
    assert result == 'roofs'


def test_pluralize_noun_belief():
    result = plurals.pluralize_noun('belief')
    assert result == 'beliefs'


def test_pluralize_noun_chef():
    result = plurals.pluralize_noun('chef')
    assert result == 'chefs'


def test_pluralize_noun_chief():
    result = plurals.pluralize_noun('chief')
    assert result == 'chiefs'


def test_pluralize_noun_gas():
    result = plurals.pluralize_noun('gas')
    assert result == 'gasses'


def test_pluralize_noun_fez():
    result = plurals.pluralize_noun('fez')
    assert result == 'fezzes'


def test_pluralize_noun_photo():
    result = plurals.pluralize_noun('photo')
    assert result == 'photos'


def test_pluralize_noun_piano():
    result = plurals.pluralize_noun('piano')
    assert result == 'pianos'


def test_pluralize_noun_halo():
    result = plurals.pluralize_noun('halo')
    assert result == 'halos'


def test_pluralize_noun_tooth():
    result = plurals.pluralize_noun('tooth')
    assert result == 'teeth'
