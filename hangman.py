#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Hangman Puzzle
# 
# Boubakr NOUR <n.boubakr@gmail.com>

import os
import random

hangman_pic = ["""
  +---+
  |   |
      |
      |
      |
      |
=========""", """
  +---+
  |   |
  0   |
      |
      |
      |
=========""", """
  +---+
  |   |
  0   |
  |   |
      |
      |
=========""", """
  +---+
  |   |
  0   |
 /|   |
      |
      |
=========""", """
  +---+
  |   |
  0   |
 /|\  |
      |
      |
=========""", """
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========""", """
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
========="""]

def clear():
	"""Function to clear the Terminal (Console), works under Windows, Mac OS, *Unix
	"""
	os.system(['clear', 'cls'][os.name == 'nt'])

def findChar(string, char):
	"""Find all the position for a char in string, and return them in a list
	"""
	return [position for position, letter in enumerate(string) if letter == char]

def main():
	play_again = True
	print "Welcome to The Hangman !\n"
	while play_again:
		print "Choose a category:\n1- Verbs\n2- Adjectives\n3- Animals\n4- Cities\n5- Countries\n"
		category_choose = int(raw_input("Your choose: "))
		while category_choose not in range(1, 6):
			category_choose = int(raw_input("Your choose: "))

		if category_choose == 1:
			dict_file = open('wordlists/verbs.txt', 'r')
		elif category_choose == 2:
			dict_file = open('wordlists/adjectives.txt', 'r')
		elif category_choose == 3:
			dict_file = open('wordlists/animals.txt', 'r')
		elif category_choose == 4:
			dict_file = open('wordlists/cities.txt', 'r')
		elif category_choose == 5:
			dict_file = open('wordlists/countries.txt', 'r')

		# Load all words from wordlist file
		words = dict_file.readlines()
		rand_int = random.randint(0, len(words))

		secret_word = words[rand_int].strip()
		#
		# TODO: Need to optimise the word that has blank space !
		#
		display_word = ['-'] * len(secret_word)

		# Number of possible tries
		tries = 7
		# A list for all the used letters
		used_letters = list()

		while True:
			if tries == 0:
				print "\n[!] Guesser loses - The answer was:", secret_word.upper()
				break
			elif '-' not in display_word:
				print "\n[!] Correct Guess !"
				print "[!] Get it with %d wrong guess !" % (7 - tries)
				break

			clear()
			print hangman_pic[7 - tries]
			print "\nWord:", ''.join(display_word).upper()
			print "Misses:,", ", ".join(used_letters)
			# Get only the first char
			letter = raw_input('Guess: ').lower().strip()[0]
			
			if letter in used_letters:
				print "[!] You already used this letter, try another !"
				continue
			elif letter in secret_word:
				print "[!] Correct Guess"
				used_letters.append(letter)
				letter_positions = findChar(secret_word, letter)
				for pos in letter_positions:
					display_word[pos] = str(letter)
			else:
				print '[!] Wrong Guess...'
				used_letters.append(letter)
				tries -= 1

		playAgain = raw_input("\nDo you want to play again (y/n)? ").lower().strip()
		while playAgain not in ('y', 'yes', 'n', 'no'):
			playAgain = raw_input("Do you want to play again (y/n)? ").lower().strip()

		if playAgain in ('y', 'yes'):
			play_again = True
			clear()
		elif playAgain in ('n', 'no'):
			play_again = False


if __name__ == '__main__':
	main()