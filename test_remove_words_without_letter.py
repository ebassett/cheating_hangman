#!/usr/bin/env python

def remove_words_without_letter(wordlist, required_letter):
    ''' # doctest
    >>> remove_words_without_letter(word_list, 'a')
    ['bat']
    >>> remove_words_without_letter(word_list, 'b')
    ['bat', 'bet', 'bit', 'bot', 'but', 'byte']
    >>> remove_words_without_letter(word_list, 'e')
    ['bet', 'byte']
    >>> remove_words_without_letter(word_list, 'z')
    []
    '''

    # Design decision: Do NOT update the list *in place*; return a new list
    updated_list = [word for word in wordlist if required_letter in word]
    return updated_list


if __name__ == '__main__':
    import doctest
    word_list = ['bat', 'bet', 'bit', 'bot', 'but', 'byte']
    doctest.testmod(verbose=True)

