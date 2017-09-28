import rhymes


# Tests for def rhyme(inp, level):
def test_rhyme_bat():
    word = 'bat'
    results = rhymes.rhyme(word, 2)
    assert 'at' in results
    assert 'bat' in results
    assert 'cat' in results
    assert 'chat' in results
    assert 'fat' in results
    assert 'hat' in results
    assert 'gnat' in results
    assert 'splat' in results


def test_rhyme_bone():
    word = 'bone'
    results = rhymes.rhyme(word, 2)
    assert 'phone' in results
    assert 'bone' in results
    assert 'tone' in results
    assert 'cone' in results
    assert 'condone' in results
    assert 'loan' in results
    assert 'moan' in results

# Tests for def is_rhyme(word1, word2):
# Tests for def find_rhyme(word):
