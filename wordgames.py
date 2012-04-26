#!/usr/bin/env python

###########################-Word Games-#################################
#Copyright (C) 2011-2012, Spencer Wood <spencer.wood25@gmail.com>      #
#This program is free software: you can redistribute it and/or modify  #
#it under the terms of the Lesser GNU General Public License as        #
#published by the Free Software Foundation, either version 3 of the    #
#License, or (at your option) any later version.                       #
#                                                                      #
#This program is distributed in the hope that it will be useful,       #
#but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#GNU General Public License for more details.                          #
#                                                                      #
#You should have received a copy of the GNU General Public License     #
#along with this program.  If not, see <http://www.gnu.org/licenses/>. #
#                                                                      #
#For your convience, the LGPL license can be found on the GNU website, #
#or read http://www.gnu.org/licenses/lgpl.txt.                         #
########################################################################

import random
import linecache

def game():
	quit = False
	score = loadPlayerData()
	while quit == False:
		print "\n"*1000
		print "Your current score is: {}".format(score)
		print "\nEnter the number of the game you wish to play:\n\n1. Word Scramble\n2. Hangman\n\n"
		input = raw_input()
		if input == '1':
			score += wordScramble()
		if input == '2':
			score += hangman()
		print "\nWould you like to continue?\ny/n?\n\nScore: {}\n".format(score)
		input = raw_input()
		if input == 'y':
			savePlayerData(score)
			continue
		else:
			quit = True
	savePlayerData(score)
	
def loadPlayerData():
	playerData = open('data/player/score.dat', "r")
	score = playerData.readline()
	playerData.close()
	return int(score)
	
def savePlayerData(score):
	score = str(score)
	playerData = open('data/player/score.dat', "w")
	playerData.write(score)
	playerData.close()
	
	
def wordSelect():
	wordList = open('data/list/words.dat', "r")
	lines = fileLength(wordList)
	wordList.close()
	
	word = linecache.getline('data/list/words.dat', random.randrange(0, lines)).strip()
	
	a =[]
	for i in range(len(word)):
		a.append(word[i])
	
	random.shuffle(a)
	scrambled = ''.join(a)
	return word, scrambled
	
	
def fileLength(file):
	for i, length in enumerate(file):
		pass
	return i+1
	
def wordScramble():
	words = wordSelect()
	
	guess = ''
	tries = 0
	
	while guess != words[0]:
		print "\n" *1000
		print "Unscramble the word!\n\nScrambled word: {}".format(words[1])
		tries += 1
		guess = str(raw_input())
		if guess == (words[0]):
			print "\nYou win!"
			return 1
		if guess != words[0]:
			print "Sorry, try again!\n"
		if tries == 10:
			print "Out of tries!"
			return 0
	
def hangman():
	word = wordSelect()
	word = word[0]
	unsolved = []
	solution = []
	tries = 9
	tried = []
	for i in range(len(word)):
		unsolved.append('_')
		solution.append(word[i])
	
	while unsolved != solution:
		print '\n'*1000
		print ' '.join(unsolved)
		print '\n'*10
		print ' '.join(tried)
		print "\n\nTries remaining: {}/10".format(tries)
		guess = raw_input()
		guess += ' '

		if not guess[0] in word:
			tries -= 1
			
		if tries < 1:
			print "out of tries!"
			print "the word was: {}".format(''.join(solution))
			raw_input()
			return 0
			
		tried.append(guess[0])
		for i in range(len(word)):
			if guess[0] == solution[i]:
				unsolved[i] = guess[0]

	print "Letters Tried: {}".format(' '.join(tried))
	print ''.join(unsolved)
	return 1

if __name__ == "__main__":
	game()






