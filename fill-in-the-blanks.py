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

# Wraps printing of paragraphs
def prettyPrint(list):
	print ""
	wrapper = textwrap.wrap(list, width=60)
	for e in wrapper:
		print e
	print ""
	
def userAnswers():
	numberOfGuesses = 5
	answer = []
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
	
def finalMessage():
	if numberOfGuesses > 0:
		print ""
		print "Congratulations! You filled in all of the blanks."
		print ""
	else:
		print ""
		print "Sorry. Out of guesses. Try again."
		print ""

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
numberOfGuesses = userAnswers()
finalMessage()


