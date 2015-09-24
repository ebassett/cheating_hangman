#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Think Like a Programmer ex8.1
# PROBLEM: CHEATING AT HANGMAN
# Write a program that will be Player 1 in a text-based version of hangman (that is, you
# don't actually have to draw a hanged man—just keep track of the number of incorrect
# guesses). Player 2 will set the difficulty of the game by specifying the length of the
# word to guess as well as the number of incorrect guesses that will lose the game.
# The twist is that the program will cheat. Rather than actually picking a word at
# the beginning of the game, the program may avoid picking a word, so long as when
# Player 2 loses, the program can display a word that matches all the information given
# to Player 2. The correctly guessed letters must appear in their correct positions, and
# none of the incorrectly guessed letters can appear in the word at all. When the game
# ends, Player 1 (the program) will tell Player 2 the word that was chosen. Therefore,
# Player 2 can never prove that the game is cheating; it's just that the likelihood of Player 2
# winning is small.

from __future__ import print_function
import argparse
import bisect  # For weighted_choice(_)
from enum import Enum  # `pip install enum34` to get this module (or delete the log class/method/calls to do without)
import random
import sys


class Log(Enum):
    ERROR   = 0
    WARNING = 1
    INFO    = 2
    DEBUG   = 3

    def __str__(self):
        return self.name


def log(LEVEL, *objs):
    print(str(LEVEL) + ':', *objs, file=sys.stderr)



def parse_args():
    parser = argparse.ArgumentParser(description='HANGMAN - optionally set any of: word length, maximum incorrect guesses, filename of wordlist')
    parser.add_argument('-l', '--length', type=int, dest='word_length',       metavar='WORD_LENGTH',       help='The number of letters in the word')
    parser.add_argument('-m', '--misses', type=int, dest='max_misses',        metavar='MAX_WRONG_GUESSES', help='The number of incorrect guesses allowed')
    parser.add_argument('-f', '--file',             dest='wordlist_filename', metavar='WORDLIST_FILENAME', help='The filename of the wordlist')
    args = parser.parse_args()
    return args


def read_wordlist(filename):
    try:
        with open(filename, 'r') as f:
            words = []
            for line in f:
                line = line.strip()  # Stripping carriage-returns is important! (and blank lines)
                if line:
                    words.append(line)
            return words
    except IOError:
        log(Log.ERROR, 'File "{}" not found.'.format(filename))
        sys.exit(-1)


def print_wordlist(wordlist):
    print(wordlist)


def determine_word_length_frequencies(wordlist):
    '''
    :return: List of tuples of format: (word-length, frequency (ie. raw count))
    '''
    frequencies = {}
    for word in wordlist:
        length = len(word)
        frequencies[length] = frequencies.get(length, 0) + 1
    if 0 in frequencies:  # Raging paranoia: make sure there's no entry for zero-letter words
        frequencies.pop(0, 0)
    #log(Log.DEBUG, sorted(frequencies.items()))
    return frequencies.items()


def weighted_choice(choices):
    '''
    :type choices: List of tuples of format: (value, weight)
    '''
    # From http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice/4322940#4322940
    values, weights = zip(*choices)
    total = 0
    cumulative_weights = []
    for weight in weights:
        total += weight
        cumulative_weights.append(total)
    x = random.random() * total
    i = bisect.bisect(cumulative_weights, x)
    return values[i]


def count_words_without_letter(wordlist, letter):
    count = 0
    for word in wordlist:
        if letter not in word:
            count += 1
    return count


def remove_words_of_wrong_length(wordlist, acceptable_length):
    # Design decision: Do NOT update the list *in place*; return a new list
    updated_list = [word for word in wordlist if len(word) == acceptable_length]
    return updated_list


def remove_words_without_letter(wordlist, required_letter):
    # Design decision: Do NOT update the list *in place*; return a new list
    updated_list = [word for word in wordlist if required_letter in word]
    return updated_list


def remove_words_with_letter(wordlist, forbidden_letter):
    # Design decision: Do NOT update the list *in place*; return a new list
    updated_list = [word for word in wordlist if forbidden_letter not in word]
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


def most_freq_pattern_by_letter(wordlist, letter):
    ''' Determine the pattern of the word at the head of the list; count how many other words have the same pattern;
    delete those words from the list as you go; repeat with the new head until the list is empty.
    :return: the most frequent pattern and its count
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


def reduce_wordlist_by_pattern(wordlist, letter, pattern):
    reduced_list = [word for word in wordlist if matches_pattern(word, letter, pattern)]
    return reduced_list


def display_misses(letter_set, word_so_far):
    misses = [letter for letter in letter_set if letter not in word_so_far]
    print('Incorrect: {}'.format(' '.join(sorted(misses))))




if __name__ == '__main__':
    args = parse_args()
    #log(Log.DEBUG, 'Args: ', args)
    # Missing or invalid values will be corrected later, before use.
    wordlist_filename = args.wordlist_filename
    word_length = args.word_length
    max_misses = args.max_misses

    misses = 0
    discovered_letter_count = 0
    guessed_letters = set()
    current_guess = ''

    if not wordlist_filename:
        wordlist_filename = 'wordlist.txt'
    wordlist = read_wordlist(wordlist_filename)
    #log(Log.DEBUG, print_wordlist(wordlist))
    if not wordlist:
        log(Log.ERROR, 'Wordlist "{}" is empty.'.format(wordlist_filename))
        sys.exit(-1)

    # Weighted random word_length if no or invalid command-line length specified
    if not word_length  or  word_length <= 0:
        word_length_frequencies = determine_word_length_frequencies(wordlist)
        word_length = weighted_choice(word_length_frequencies)

    if max_misses < 0:
        max_misses = 8  # TODO: formula-based (somehow) on word-length

    revealed_word = '*' * word_length

    wordlist = remove_words_of_wrong_length(wordlist, word_length)
    if not wordlist:
        log(Log.ERROR, 'Wordlist "{}" contains no words of length {}.'.format(wordlist_filename, word_length))
        sys.exit(-1)

    print('HANGMAN\nThe word is {} letters long, and you are allowed {} incorrect guesses.'.format(word_length, max_misses))

    # Main game loop
    while discovered_letter_count < word_length  and  misses < max_misses:
        # Don't allow empty or invalid or previous guesses
        while (not current_guess  or
                       current_guess not in 'abcdefghijklmnopqrstuvwxyz'  or
                       current_guess in guessed_letters  or
                       len(current_guess) != 1):
            current_guess = raw_input('Letter to guess: ').lower()
        guessed_letters.add(current_guess)

        count_of_words_without_letter = count_words_without_letter(wordlist, current_guess)
        current_pattern = list()
        current_pattern_count = 0
        (current_pattern, current_pattern_count) = most_freq_pattern_by_letter(wordlist, current_guess)
        if count_of_words_without_letter > current_pattern_count:  # ie. eliminating this letter leaves more options than including it
            wordlist = remove_words_with_letter(wordlist, current_guess)
            misses += 1
        else:
            for index in current_pattern:
                discovered_letter_count += 1
                revealed_word = revealed_word[0:index] + current_guess + revealed_word[index + 1:]
            wordlist = reduce_wordlist_by_pattern(wordlist, current_guess, current_pattern)

        print('Word so far: {}'.format(revealed_word))
        display_misses(guessed_letters, revealed_word)

        if max_misses - misses == 1:
            print('WARNING: Last guess (if incorrect)!')

    if misses >= max_misses:
        print('\nYOU LOSE! The word was "{}".'.format(random.choice(wordlist)))
    else:
        print('\nYOU WIN!')


'''
FUTURE WORK
- Calculate "optimal" max_misses by (some!) formula based on word length
- Graphics?
'''

# vim: expandtab shiftwidth=4 softtabstop=4 tabstop=4
