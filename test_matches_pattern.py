#!/usr/bin/env python

def is_number_in_pattern(pattern, number):
    if number in pattern:
        return True
    else:
        return False


def matches_pattern(word, letter, pattern):
    ''' # doctest
    >>> matches_pattern('odd', 'd', [1, 2])
    True
    >>> matches_pattern('odd', 'd', [1])
    False
    >>> matches_pattern('odd', 'd', [0, 1, 2])
    False
    >>> matches_pattern('odd', 'd', [1, 2, 3])
    False
    '''

    if max(pattern) >= len(word) or min(pattern) < 0:  # Paranoid edge cases
        return False

    for i in xrange(len(word)):
        if word[i] == letter:
            if not is_number_in_pattern(pattern, i):
                return False
        elif is_number_in_pattern(pattern, i):
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

