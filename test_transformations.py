import transformations as tr


def test_to_ing_tense_rip():
    assert tr.to_ing_tense('rip') == 'ripping'


def test_to_ing_tense_walk():
    assert tr.to_ing_tense('walk') == 'walking'


def test_to_ing_tense_run():
    assert tr.to_ing_tense('run') == 'running'


def test_to_ing_tense_hum():
    assert tr.to_ing_tense('hum') == 'humming'


def test_to_ing_tense_breathe():
    assert tr.to_ing_tense('breathe') == 'breathing'


def test_to_ing_tense_create():
    assert tr.to_ing_tense('create') == 'creating'


def test_to_ing_tense_hope():
    assert tr.to_ing_tense('hope') == 'hoping'


def test_to_ing_tense_hop():
    assert tr.to_ing_tense('hop') == 'hopping'


def test_to_ing_tense_fly():
    assert tr.to_ing_tense('fly') == 'flying'


def test_to_ing_tense_whiz():
    assert tr.to_ing_tense('whiz') == 'whizzing'


def test_to_ing_tense_lead():
    assert tr.to_ing_tense('lead') == 'leading'


def test_verb_to_noun_rip():
    assert tr.verb_to_noun('rip') == 'ripper'


def test_verb_to_noun_walk():
    assert tr.verb_to_noun('walk') == 'walker'


def test_verb_to_noun_run():
    assert tr.verb_to_noun('run') == 'runner'


def test_verb_to_noun_hum():
    assert tr.verb_to_noun('hum') == 'hummer'


def test_verb_to_noun_breathe():
    assert tr.verb_to_noun('breathe') == 'breather'


def test_verb_to_noun_create():
    assert tr.verb_to_noun('create') == 'creator'


def test_verb_to_noun_hope():
    assert tr.verb_to_noun('hope') == 'hoper'


def test_verb_to_noun_hop():
    assert tr.verb_to_noun('hop') == 'hopper'


def test_verb_to_noun_fly():
    assert tr.verb_to_noun('fly') == 'flyer'


def test_verb_to_noun_whiz():
    assert tr.verb_to_noun('whiz') == 'whizzer'


def test_verb_to_noun_lead():
    assert tr.verb_to_noun('lead') == 'leader'


def test_to_past_tense():
    pass


# Tests for def pluralize_noun(n):

def test_pluralize_noun_bat():
    result = tr.pluralize_noun('bat')
    assert result == 'bats'


def test_pluralize_noun_sky():
    result = tr.pluralize_noun('sky')
    assert result == 'skies'


def test_pluralize_noun_deer():
    result = tr.pluralize_noun('deer')
    assert result == 'deer'


def test_pluralize_noun_mouse():
    result = tr.pluralize_noun('mouse')
    assert result == 'mice'


def test_pluralize_noun_roof():
    result = tr.pluralize_noun('roof')
    assert result == 'roofs'


def test_pluralize_noun_belief():
    result = tr.pluralize_noun('belief')
    assert result == 'beliefs'


def test_pluralize_noun_chef():
    result = tr.pluralize_noun('chef')
    assert result == 'chefs'


def test_pluralize_noun_chief():
    result = tr.pluralize_noun('chief')
    assert result == 'chiefs'


def test_pluralize_noun_gas():
    result = tr.pluralize_noun('gas')
    assert result == 'gasses'


def test_pluralize_noun_fez():
    result = tr.pluralize_noun('fez')
    assert result == 'fezzes'


def test_pluralize_noun_photo():
    result = tr.pluralize_noun('photo')
    assert result == 'photos'


def test_pluralize_noun_piano():
    result = tr.pluralize_noun('piano')
    assert result == 'pianos'


def test_pluralize_noun_halo():
    result = tr.pluralize_noun('halo')
    assert result == 'halos'


def test_pluralize_noun_tooth():
    result = tr.pluralize_noun('tooth')
    assert result == 'teeth'
