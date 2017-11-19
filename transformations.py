from nltk.corpus import cmudict

DOUBLERS = ('b', 'd', 'g', 'm', 'n', 'p', 't', 'z')
DOUBLING_EXCEPTIONS = ('mb', 'ng', 'en')
VOWELS = ('a', 'e', 'i', 'o', 'u')

d = cmudict.dict()


def double_up_con(word, suffix):
    return word[:-1] + word[-1] * 2 + suffix


def to_past_tense(verb):
    """ Takes a present tense verb and changes it to past tense 'ed' or similar. """
    if verb in past_tense_exceptions:
        return past_tense_exceptions[verb]
    elif verb.endswith('e'):
        return verb + 'd'
    elif verb.endswith(DOUBLING_EXCEPTIONS):
        return verb + 'ed'
    elif verb.endswith(DOUBLERS):
        return double_up_con(verb, 'ed')
    else:
        return verb + 'ed'


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


def count_syllables(word):
    # print("lookin up: '{}'".format(word))
    lookup = d.get(word.lower(), None)
    # print("result: {}".format(lookup))

    if lookup:
        return len(list(x for x in lookup.pop() if x[-1].isdigit()))
    else:
        return -1


def too_wordy(word1, word2):
    word1_ct = count_syllables(word1)
    word2_ct = count_syllables(word2)

    # print('{} = {}, {} = {}'.format(word1, word1_ct, word2, word2_ct))

    if word1_ct == -1 or word2_ct == -1:
        return False
    elif word1_ct >= 3 and word2_ct >= 4:
        return True
    else:
        return False


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
    'lead': 'led',
    'swim': 'swam',
    'run': 'ran',
    'fly': 'flown',  # flown
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
    'ion': 'ions'
}
