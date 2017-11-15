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


def test_verb_to_noun():
    pass


def test_to_past_tense():
    pass
