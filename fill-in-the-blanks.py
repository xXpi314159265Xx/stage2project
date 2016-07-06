# coding: utf-8
# IPND Stage 2 Final Project

import textwrap

paragraphs = {'easy':"The ___1___ value of a number is its ___2___ from zero " 
			"on the ___3___ line. Absolute value is always ___4___ ."
			" The absolute value of a positive number is ___4___ and the"
			" absolute value of a ___5___ number is ___4___ .", 
			'medium': "To solve an ___1___ with absolute value you solve "
			"___2___ equations. Therefore, usually there are ___2___ answers. " 
			"In order to get these ___2___ answers you have to ___3___ the "
			"absolute value part of the equation and change the ___4___ of "
			"the number(s) without the absolute value symbol.", 
			'hard': "To solve an absolute value ___1___ you solve two "
			"___2___ , but they are written as ___3___ ___2___ ."
			"The symbol < transforms the absolute value ___1___ into "
			"a ___3___ inequality joined by the word ' ___4___ '. The symbol > "
			"transforms the absolute value ___1___ into a ___3___ "
			"inequality joined by the word ' ___5___ '."}

easyAnswers = ['absolute', 'distance', 'number', 'positive', 'negative']
mediumAnswers = ['equation', 'two', 'isolate', 'sign']
hardAnswers = ['inequality', 'inequalities', 'compound', 'and', 'or']

# Function returns difficulty of quiz selected by the user.
def levelSelect():
    levels = ['easy', 'medium', 'hard']
    while True:
        difficulty = str(raw_input()).lower()
        if difficulty not in levels:
            print "Please type easy, medium or hard."
        else:
            break
    return difficulty

# Take a list as input and wraps printing of paragraphs
def prettyPrint(list):
	print ""
	wrapper = textwrap.wrap(list, width=60)
	for e in wrapper:
		print e
	print ""

# User chooses between 1 and 20 guesses for the quiz
def numberOfGuesses():
	while True:
		try:
			userGuesses = int(raw_input("How many guesses would you like "
			"to have in order to try to fill in all of the blanks? \n"))
			assert (userGuesses < 21 and userGuesses > 0)
		except ValueError:
			print "You must enter an integer."
			continue
		except AssertionError:
			print "You may have 1 - 20 guesses."
			continue
		else:
			return userGuesses

# Takes the number of guesses as input and user guesses answers to blanks
# until all of the blanks are filled or the user runs out of guesses.
def userAnswers(numberOfGuesses):
	blank = 1
	print "You begin the game with " + str(numberOfGuesses) + " guesses."
	print ""
	for word in questions:
		while numberOfGuesses > 0 and word == "___" + str(blank) + "___":
			response = raw_input("What is the answer to blank " \
			+ str(blank) + "\n").lower()
			if response == answerList[blank-1]:
				print ""
				print "Correct!"
				print ""
				print "You still have " + str(numberOfGuesses) + " guesses left."
				print ""
				while "___" + str(blank) + "___" in questions:
					index = questions.index("___" + str(blank) + "___")
					questions[index] = response
				blank += 1
				prettyPrint(" ".join(questions))
			else:
				numberOfGuesses -= 1
				print ""
				prettyPrint(" ".join(questions))
				print "Incorrect. You have " + str(numberOfGuesses) + \
				" guesses left."
	return numberOfGuesses

# Displays a winning or losing message based on how many guesses are remaining	
def finalMessage():
	if remainingGuesses > 0:
		print ""
		print "Congratulations! You filled in all of the blanks."
		print ""
	else:
		print ""
		print "Sorry. Out of guesses. Try again."
		print ""

# Takes the user chosen difficulty as input and returns the list with the 
# answers for that level.
def chooseAnswers(difficulty):
	if difficulty == "easy":
		return easyAnswers
	elif difficulty == "medium":
		return mediumAnswers
	else:
		return hardAnswers

print "Please select a game difficulty by typing it in."
print "Possible choices include easy, medium and hard."
difficulty = levelSelect()
answerList = chooseAnswers(difficulty)
prettyPrint(paragraphs[difficulty])
questions = paragraphs[difficulty].split()
numberOfGuesses = numberOfGuesses()
remainingGuesses = userAnswers(numberOfGuesses)
finalMessage()


