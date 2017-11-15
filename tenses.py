
def to_past_tense(verb):
    """ Takes a present tense verb and changes it to past tense 'ed' or similar. """


def to_ing_tense(verb):
    """ Takes a present tense verb and adds the suffix 'ing' """
    if verb.endswith('e'):
        return verb[:-1] + 'ing'
    elif verb.endswith(('b', 'd', 'g', 'p', 't')):
        return verb[:-1] + verb[-1] * 2 + 'ing'
    else:
        return verb + 'ing'


def verb_to_noun(verb):
    """ Takes a noun and adds the suffix 'er' to transform it into a noun. """


past_tense_exceptions = {
    'drive': 'drove',
    'dive': 'dove',
    'eat': 'ate',
    'bite': 'bit',
    'swim': 'swam',
    'run': 'ran',
    'fly': 'flew',  # flown
    'fight': 'fought',
    'sew': 'sewn',
    'see': 'saw',  # seen
    'throw': 'threw',  # thrown
}
