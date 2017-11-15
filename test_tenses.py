import tenses


def test_to_ing_tense_rip():
    assert tenses.to_ing_tense('rip') == 'ripping'


def test_to_ing_tense_walk():
    assert tenses.to_ing_tense('walk') == 'walking'


def test_to_ing_tense_breathe():
    assert tenses.to_ing_tense('breathe') == 'breathing'


def test_to_ing_tense_create():
    assert tenses.to_ing_tense('create') == 'creating'


def test_to_ing_tense_hope():
    assert tenses.to_ing_tense('hope') == 'hoping'


def test_to_ing_tense_hop():
    assert tenses.to_ing_tense('hop') == 'hopping'


def test_to_ing_tense_fly():
    assert tenses.to_ing_tense('fly') == 'flying'


def test_verb_to_noun_rip():
    assert tenses.verb_to_noun('rip') == 'ripper'


def test_verb_to_noun_walk():
    assert tenses.verb_to_noun('walk') == 'walker'


def test_verb_to_noun_breathe():
    assert tenses.verb_to_noun('breathe') == 'breather'


def test_verb_to_noun_create():
    assert tenses.verb_to_noun('create') == 'creator'


def test_verb_to_noun_hope():
    assert tenses.verb_to_noun('hope') == 'hoper'


def test_verb_to_noun_hop():
    assert tenses.verb_to_noun('hop') == 'hopper'


def test_verb_to_noun_fly():
    assert tenses.verb_to_noun('fly') == 'flyer'


def test_to_past_tense():
    pass
