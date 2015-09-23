#!/usr/bin/env python

def count_words_without_letter(wordlist, letter):
    '''' # doctest
    >>> count_words_without_letter(word_list, 'a')
    4
    >>> count_words_without_letter(word_list, 'b')
    0
    '''

    count = 0
    for word in wordlist:
        if letter not in word:
            count += 1
    return count


if __name__ == '__main__':
    import doctest
    word_list = ['bat', 'bet', 'bit', 'bot', 'but']
    doctest.testmod(verbose=True)

