# Cheating Hangman

This is a python (2) implementation of Exercise 8.1 from the book Think Like a Programmer.

Write a program that will be Player 1 in a text-based version of hangman (that is, you don't actually have to draw a hanged man—just keep track of the number of incorrect guesses). Player 2 will set the difficulty of the game by specifying the length of the word to guess as well as the number of incorrect guesses that will lose the game.  
**The twist is that the program will cheat.** Rather than actually picking a word at the beginning of the game, the program may avoid picking a word, so long as when Player 2 loses, the program can display a word that matches all the information given to Player 2. The correctly guessed letters must appear in their correct positions, and none of the incorrectly guessed letters can appear in the word at all. When the game ends, Player 1 (the program) will tell Player 2 the word that was chosen. Therefore, Player 2 can never prove that the game is cheating; it's just that the likelihood of Player 2 winning is small.

