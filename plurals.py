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
    'deer': 'deer'
}

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



