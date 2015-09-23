#!/usr/bin/env python

def remove_words_with_letter(wordlist, forbidden_letter):
    ''' # doctest
    >>> remove_words_with_letter(word_list, 'a')
    ['bet', 'bit', 'bot', 'but', 'byte']
    >>> remove_words_with_letter(word_list, 'b')
    []
    >>> remove_words_with_letter(word_list, 'e')
    ['bat', 'bit', 'bot', 'but']
    >>> remove_words_with_letter(word_list, 'z')
    ['bat', 'bet', 'bit', 'bot', 'but', 'byte']
    '''

    # Design decision: Do NOT update the list *in place*; return a new list
    updated_list = [word for word in wordlist if forbidden_letter not in word]
    return updated_list


if __name__ == '__main__':
    import doctest
    word_list = ['bat', 'bet', 'bit', 'bot', 'but', 'byte']
    doctest.testmod(verbose=True)

