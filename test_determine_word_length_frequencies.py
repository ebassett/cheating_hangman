#!/usr/bin/env python

def determine_word_length_frequencies(wordlist):
    '''' # doctest
    >>> determine_word_length_frequencies(wordlist)
    [(3, 5), (4, 1)]
    >>> determine_word_length_frequencies(wordlist2)
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    >>> determine_word_length_frequencies(wordlist3)
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]
    '''

    frequencies = {}
    for word in wordlist:
        length = len(word)
        frequencies[length] = frequencies.get(length, 0) + 1
    if 0 in frequencies:  # Raging paranoia: make sure there's no entry for zero-letter words
        frequencies.pop(0, 0)
    return sorted(frequencies.items())  # EJB: sorted here only for reproduceability for doctest



if __name__ == '__main__':
    import doctest
    wordlist = ['bat', 'bet', 'bit', 'bot', 'but', 'byte']
    wordlist2 = ['a', 'bb', 'ba', 'ccc', 'cca', 'cba', 'dddd', 'dddc', 'ddcb', 'dcba', 'eeeee', 'eeeed', 'eeedc', 'eedcb', 'edcba']
    wordlist3 = ['', 'a', 'bb', 'ba', 'ccc', 'cca', 'cba', 'dddd', 'dddc', 'ddcb', 'dcba', 'eeeee', 'eeeed', 'eeedc', 'eedcb', 'edcba']
    doctest.testmod(verbose=True)

