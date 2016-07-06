# coding: utf-8
# IPND Stage 2 Final Project

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

import textwrap

print "Please select a game difficulty by typing it in."
print "Possible choices include easy, medium and hard."

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

difficulty = levelSelect()

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

# Wraps printing of paragraphs
def prettyPrint(list):
	print ""
	wrapper = textwrap.wrap(list, width=60)
	for e in wrapper:
		print e
	print ""
		
prettyPrint(paragraphs[difficulty])

questions = paragraphs[difficulty].split()

if difficulty == "easy":
	answerList = easyAnswers
elif difficulty == "medium":
	answerList = mediumAnswers
else:
	answerList = hardAnswers

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
				#indices = [i for i,val in enumerate(questions) if val=="___" \
				#+ str(blank) + "___"]
				#print indices
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
	if numberOfGuesses > 0:
		print ""
		print "Congratulations! You filled in all of the blanks."
		print ""
	else:
		print ""
		print "Sorry. Out of guesses. Try again."
		print ""


userAnswers()

