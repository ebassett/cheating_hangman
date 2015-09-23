#!/usr/bin/env python

def remove_words_without_letter(wordlist, required_letter):
    # Design decision: Do NOT update the list *in place*; return a new list
    updated_list = [word for word in wordlist if required_letter in word]
    return updated_list

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


def determine_pattern(word, letter):
    pattern = []
    for i in xrange(len(word)):
        if word[i] == letter:
            pattern.append(i)
    return pattern


def mostFreqPatternByLetter(wordlist, letter):
    ''' Determine the pattern of the word at the head of the list; count how many other words have the same pattern;
    delete those words from the list as you go; repeat with the new head until the list is empty.

    #doctest
    >>> mostFreqPatternByLetter(['add', 'odd'], 'd')
    ([1, 2], 2)
    >>> mostFreqPatternByLetter(['add', 'odd', 'dad', 'did', 'dud'], 'd')
    ([0, 2], 3)
    >>> mostFreqPatternByLetter(['add', 'odd', 'dad', 'did', 'dud', 'dude'], 'd')
    ([0, 2], 4)
    >>> mostFreqPatternByLetter(['d', 'dd', 'ad', 'ddd', 'add', 'dad'], 'd')
    ([0], 1)
    '''
    temp_wordlist = remove_words_without_letter(wordlist, letter)  # Does not modify original wordlist
    max_pattern = []
    max_pattern_count = 0
    while len(temp_wordlist) > 0:
        # Determine pattern of letter in word at head of wordlist
        head_word = temp_wordlist[0]
        pattern = determine_pattern(head_word, letter)

        # For the current pattern, count and delete matches
        pattern_count = 0
        nonmatching_list = []  # Build new temp_wordlist without the words that match the current pattern

        for word in temp_wordlist:
            if matches_pattern(word, letter, pattern):
                pattern_count += 1
                # EJB: or drop the else-clause and nonmatching_list, and just do (here): temp_wordlist.remove(word)
                # EJB: TODO: time each of these variants.
            else:
                nonmatching_list.append(word)
        temp_wordlist = nonmatching_list

        if pattern_count > max_pattern_count:
            max_pattern = pattern
            max_pattern_count = pattern_count

    return (max_pattern, max_pattern_count)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

