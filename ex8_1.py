#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ex8_1 - 2015-07-25 - ejb
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
from enum import Enum
import sys

class Log(Enum):
    ERROR   = 0  #"ERROR"
    WARNING = 1  #"WARNING"
    INFO    = 2  #"INFO"
    DEBUG   = 3  #"DEBUG"

    def __str__(self):
        return self.name  # self.value


def log(LEVEL, *objs):
    print(str(LEVEL) + ":", *objs, file=sys.stderr)


def read_wordlist(filename):
    try:
        with open(filename, "r") as f:
            words = f.readlines()
            return words
    except IOError:
        log(Log.ERROR, "File '{}' not found.".format(filename))
        sys.exit(-1)


def print_wordlist(word_list):
    print(word_list)


def countWordsWithoutLetter(wordlist, letter):
    count = 0
    for word in wordlist:
        if letter not in word:
            count += 1
    return count


def removeWordsOfWrongLength(wordlist, acceptableLength):
    global word_list
    word_list = [word for word in wordlist if len(word) == acceptableLength]
    return word_list

def removeWordsWithoutLetter(wordlist, requiredLetter):
    # Note "wordlist" vs. "word_list" (with underscore)
    word_list = [word for word in wordlist if requiredLetter not in word]
    return word_list

def removeWordsWithLetter(wordlist, forbiddenLetter):
    # Note "wordlist" vs. "word_list" (with underscore)
    word_list = [word for word in wordlist if forbiddenLetter in word]
    return word_list

def numberInPattern(pattern, number):
    if number in pattern:
        return True
    else:
        return False

def matchesPattern(word, letter, pattern):
    for i in xrange(len(word)):
        if word[i] == letter:
            if not numberInPattern(pattern, i):
                return False
        elif numberInPattern(pattern, i):
            return False
    return True


def mostFreqPatternByLetter(wordlist, letter):
    ''' Determine the pattern of the word at the head of the list; count how many other words have the same pattern;
    delete those words from the list as you go; repeat with the new head until the list is empty.
    :param wordlist:
    :param letter:
    :return: the most frequent pattern and its count
    '''
    temp_word_list = wordlist[:]  # Copy of wordlist, not wordlist itself.
    temp_word_list = removeWordsWithoutLetter(temp_word_list, letter)
    maxPattern = None
    maxPatternCount = 0
    while len(temp_word_list) > 0:
        # Determine pattern of word at head of word list
        currentPattern = []
        head_word = temp_word_list[0]
        for i in xrange(len(head_word)):
            if head_word[i] == letter:
                currentPattern.append(i)
        currentPatternCount = 1
        temp_word_list.pop(i)

        for i in xrange(len(temp_word_list)):
            if matchesPattern(temp_word_list[i], letter, currentPattern):
                currentPatternCount += 1
                # EJB: This is not going to work, oder? - popping items from the list as I iterate over it
                temp_word_list.pop(i)

        if currentPatternCount > maxPatternCount:
            maxPatternCount = currentPatternCount
            maxPattern = currentPattern

    return (maxPattern, maxPatternCount)  # EJB: original used out parameters rather than return value


def displayGuessedLetters(letter_set):
    # EJB: I am using a set rather than a list of bools
    print(sorted(letter_set))







if __name__ == "__main__":
    wordLength = 8;
    maxMisses = 9;

    misses = 0;
    discoveredLetterCount = 0;

    revealedWord = "********"
    guessedLetters = set()

    word_list = read_wordlist("wordlist.txt")
    #log(Log.DEBUG, print_wordlist(word_list))
    removeWordsOfWrongLength(word_list, wordLength)

    nextLetter = ''  # Current guess

    print("Word so far: {}".format(revealedWord))

    # Main game loop
    while discoveredLetterCount < wordLength and  misses < maxMisses:
        nextLetter = raw_input("Letter to guess: ")
        guessedLetters.add(nextLetter)

        missingCount = countWordsWithoutLetter(word_list, nextLetter)
        nextPattern = list()
        nextPatternCount = 0
        (nextLetter, nextPatternCount) = mostFreqPatternByLetter(word_list, nextLetter)
        if missingCount > nextPatternCount:
            removeWordsWithLetter(word_list, nextLetter)
            misses += 1
        else:
        list<int>::iterator iter = nextPattern.begin();
        while (iter != nextPattern.end()) {
        discoveredLetterCount++;
        revealedWord[*iter] = nextLetter;
        iter++;
        }

        wordList = reduceByPattern(wordList, nextLetter, nextPattern);
        }

        print("Word so far: {}".format(revealedWord))
        displayGuessedLetters(guessedLetters)



