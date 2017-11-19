DOUBLERS = ('b', 'd', 'g', 'm', 'n', 'p', 't', 'z')
DOUBLING_EXCEPTIONS = ('mb', 'ng', 'ot', 'en')
VOWELS = ('a', 'e', 'i', 'o', 'u')


def double_up_con(word, suffix):
    return word[:-1] + word[-1] * 2 + suffix


def to_past_tense(verb):
    """ Takes a present tense verb and changes it to past tense 'ed' or similar. """


def to_ing_tense(verb):
    """ Takes a present tense verb and adds the suffix 'ing' """
    if verb.endswith('e'):
        return verb[:-1] + 'ing'  # Remove the ending e
    elif verb.endswith(DOUBLING_EXCEPTIONS):
        return verb + 'ing'
    elif verb[-3] in VOWELS and verb[-2] in VOWELS:  # No doubling for double vowels!
        return verb + 'ing'
    elif verb.endswith(DOUBLERS) and verb[-2] in VOWELS:
        return double_up_con(verb, 'ing')
    else:
        return verb + 'ing'


def verb_to_noun(verb):
    """ Takes a noun and adds the suffix 'er' to transform it into a noun. """
    if verb in er_exceptions:
        return er_exceptions[verb]
    elif verb.endswith('e'):
        return verb + 'r'
    elif verb.endswith(DOUBLING_EXCEPTIONS):
        return verb + 'er'
    elif verb[-3] in VOWELS and verb[-2] in VOWELS:
        return verb + 'er'
    elif verb.endswith(DOUBLERS) and verb[-2] in VOWELS:  # No doubling for double vowels!
        return double_up_con(verb, 'er')
    else:
        return verb + 'er'


def pluralize_noun(n):
    """ Takes a noun and turns it into it's plural form """

    # Check exceptions first:
    if n in exceptions:
        return exceptions[n]

    if n.endswith('us'):
        return n[:-2] + 'i'
    elif n.endswith('is'):
        return n[:-2] + 'es'
    elif n.endswith(('s', 'ss', 'sh', 'ch', 'x', 'z', 'o')):
        return n + 'es'
    elif n.endswith('f'):
        return n[:-1] + 'ves'
    elif n.endswith('fe'):
        return n[:-2] + 'ves'
    elif n.endswith('tion'):
        return n + 's'
    elif n.endswith('on'):
        return n[:-2] + 'a'
    elif n.endswith('y') and n[-2] in 'bcdfghjklmnpqrstvwxz':
        return n[:-1] + 'ies'
    else:
        return n + 's'


er_exceptions = {
    'create': 'creator',
    'act': 'actor',
    'mediate': 'mediator',
    'alternate': 'alternator',
    'collect': 'collector',
    'dictate': 'dictator',
    'vend': 'vendor',
    'invest': 'investor',
    'credit': 'creditor',
    'instruct': 'instructor',
    'guide': 'guide',
    'hurry': 'hurrier'
}

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


exceptions = {
    'roof': 'roofs',
    'belief': 'beliefs',
    'chef': 'chefs',
    'chief': 'chiefs',
    'gas': 'gasses',
    'fez': 'fezzes',
    'photo': 'photos',
    'piano': 'pianos',
    'halo': 'halos',
    'tooth': 'teeth',
    'mouse': 'mice',
    'deer': 'deer',
    'rodeo': 'rodeos',  # Maybe a rule for this...
}
