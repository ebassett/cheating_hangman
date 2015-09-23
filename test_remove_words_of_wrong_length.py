#!/usr/bin/env python

def remove_words_of_wrong_length(wordlist, acceptable_length):
    '''' # doctest
    >>> remove_words_of_wrong_length(word_list, 3)
    ['bat', 'bet', 'bit', 'bot', 'but']
    >>> remove_words_of_wrong_length(word_list, 4)
    ['byte']
    '''

    #global word_list
    updated_list = [word for word in wordlist if len(word) == acceptable_length]
    return updated_list


if __name__ == '__main__':
    import doctest
    word_list = ['bat', 'bet', 'bit', 'bot', 'but', 'byte']
    # NOTE: With "global" uncommented in the method, __main__ gets the modified copy of the list from doctest
    #doctest.testmod(verbose=True)
    print ''
    returned_list = remove_words_of_wrong_length(word_list, 3)
    print word_list
    print returned_list

