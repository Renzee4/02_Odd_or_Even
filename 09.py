import random




randomNum = random.randint(1, 9)

def game():
	user = int(raw_input('Pick a number between 1-9: '))
	comp = randomNum

	if user == comp:
		print "just right"
	elif user > comp:
		print "guess lower"

	elif user < comp:
		print "guess higher"


def letsPlay():
	rounds = 0
	while True:
		game()
		
		playAgain = raw_input('Guess again? (yes/no): ').lower() == 'yes'
		rounds += 1
		if not playAgain:
			print "Thanks for playing! it took you", rounds, " guess(es)."
			break

def intro():
	print " "
	print "let's play a guessing game"
	print "Try and guess what number I am thinking of between 1-9."
	beginGame = raw_input('Want to play? (yes/no): ').lower()

	if beginGame == 'yes':
		letsPlay()
	else:
		pass

intro()