import random

#rock, paper, scissors!

#rock beats scissors
#paper beats rock
#scissors beats paper

print "Let's play rock, paper, scissors"


def playGame():
	you = raw_input("Pick rock, paper, or scissors: ")
	print "You picked: " + you


	oppChoice = ['rock', 'paper', 'scissors']
	opponent = random.choice(oppChoice)
	print "Your opponent chose: " + opponent


	while you == 'rock':
		if opponent == 'paper':
			print 'YOU L.O.S.E!!'
		elif opponent == 'scissors':
			print 'you WIN :]'	
		elif opponent == 'rock':
			print "it's a draw!"
		break

	while you == 'paper':
		if opponent == 'paper':
			print "it's a draw!"
		elif opponent == 'scissors':
			print 'YOU L.OS.E!!'
		elif opponent == 'rock':
			print 'ayeee you WIN!'
		break

	while you == 'scissors':
		if opponent == 'paper':
			print 'WHOO YOU WINN!!'
		elif opponent == 'scissors':
			print "hmm.. it's a draw whatever"
		elif opponent == 'rock':
			print 'GO HOME YOU LOST'
		break



def again():

	while True:
		playGame()

		goAgain = raw_input('Play again? yes/no: ').lower() == 'yes'
		if not goAgain:
			print "Thanks for playing! :)"
			return

again()