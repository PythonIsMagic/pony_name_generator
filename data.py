
DATA_DIR = 'data'

categories = (
    '3letter',
    'adj',
    'noun',
    'noun_abstract',
    'verb',
    # 'rhyme',
    'honorific',
    'suffix',
    'compound',
    'suffix_noun',
    'suffix_verb',
)

formats = [
    ['compound'],
    # ['noun'],
    # ['adj'],
    ['big word'],

    ['noun', 'noun'],
    ['noun', 'noun_plural'],
    ['noun', 'verb'],
    ['noun', 'verb_er'],

    ['verb_ing', 'noun'],
    ['verb_ing', 'noun_plural'],

    ['adj', 'noun'],
    ['adj', 'noun_plural'],
    ['adj', 'verb'],
    ['adj', 'verb_ing'],
    ['adj', 'verb_er'],

    # Adding random 3-letter-partials
    # ['verb', '3letter', 'noun'],
    # ['3letter', 'verb', 'noun'],

    # Suffix/prefix
    # ('suffix_noun', 'noun', 'noun'),
    # ('noun', 'suffix_noun', 'noun'),
    # ('suffix_noun', 'noun', 'verb'),
    # ('noun', 'suffix_verb', 'verb'),
    # ('suffix_verb', 'verb', 'noun'),
    # ('adj', 'suffix_noun', 'noun'),
    # ('adj', 'suffix_verb', 'verb'),

    # Rhymes
    # ('noun', 'rhyme'),
    # ('verb', 'rhyme'),

    # Alliterations
    ['noun', 'alliterate noun'],
    ['noun', 'alliterate noun_plural'],
    ['noun', 'alliterate verb'],
    ['noun', 'alliterate verb_er'],

    ['verb_ing', 'alliterate noun'],
    ['verb_ing', 'alliterate noun_plural'],

    ['adj', 'alliterate noun'],
    ['adj', 'alliterate noun_plural'],
    ['adj', 'alliterate verb'],
    ['adj', 'alliterate verb_ing'],
    ['adj', 'alliterate verb_er'],
]
