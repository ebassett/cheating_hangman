#!/usr/bin/env python

def determine_pattern(word, letter):
    ''' # doctest
    >>> determine_pattern('odd', 'd')
    [1, 2]
    >>> determine_pattern('odd', 'o')
    [0]
    >>> determine_pattern('odd', 'z')
    []
    >>> determine_pattern('deadwood', 'd')
    [0, 3, 7]
    '''
    pattern = []
    for i in xrange(len(word)):
        if word[i] == letter:
            pattern.append(i)
    return pattern


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

