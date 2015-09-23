#!/usr/bin/env python

def is_number_in_pattern(pattern, number):
    if number in pattern:
        return True
    else:
        return False

def matches_pattern(word, letter, pattern):
    if max(pattern) >= len(word)  or  min(pattern) < 0:  # Paranoid edge cases
        return False

    for i in xrange(len(word)):
        if word[i] == letter:
            if not is_number_in_pattern(pattern, i):
                return False
        elif is_number_in_pattern(pattern, i):
            return False
    return True


def reduce_wordlist_by_pattern(wordlist, letter, pattern):
    '''' # doctest
    >>> reduce_wordlist_by_pattern(wordlist, 'a', [1])
    ['bat']
    >>> reduce_wordlist_by_pattern(wordlist, 'b', [0])
    ['bat', 'bet', 'bit', 'bot', 'but']
    >>> reduce_wordlist_by_pattern(wordlist, 'b', [1, 2])
    ['abby', 'abbot']
    >>> reduce_wordlist_by_pattern(wordlist, 'z', [1])
    []
    '''

    reduced_list = [word for word in wordlist if matches_pattern(word, letter, pattern)]
    return reduced_list


if __name__ == '__main__':
    import doctest
    wordlist = ['bat', 'bet', 'bit', 'bot', 'but', 'abby', 'abbot', 'bbb']
    doctest.testmod(verbose=True)

