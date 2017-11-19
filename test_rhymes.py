import pytest
import random
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


def test_is_rhyme_bat_bat():
    result = rhymes.is_rhyme('bat', 'bat')
    assert result is False  # Can't rhyme the same word!


def test_is_rhyme_bat_cat():
    result = rhymes.is_rhyme('bat', 'cat')
    assert result is True


def test_is_rhyme_bat_bate():
    result = rhymes.is_rhyme('bat', 'bate')
    assert result is False


def test_is_rhyme_glue_unglue():
    result = rhymes.is_rhyme('glue', 'unglue')
    assert result is False


def test_is_rhyme_glue_flew():
    result = rhymes.is_rhyme('glue', 'flew')
    assert result is True


@pytest.mark.skip()
def test_is_rhyme_glue_flu():
    result = rhymes.is_rhyme('glue', 'flu')
    assert result is True


@pytest.mark.skip()
def test_is_rhyme_glue_threw():
    result = rhymes.is_rhyme('glue', 'threw')
    assert result is True


# Tests for def find_rhyme(word):
@pytest.mark.skip()
def test_find_rhyme_bat():
    results = list(rhymes.rhyme('bat', 2))
    assert rhymes.is_rhyme('bat', random.choice(results))
