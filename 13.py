a = [1, 1] 

def fibonnaci(sumlist):
	n = int(raw_input('pick a number: '))
	i = 1
	while i < n:
		newList = sumlist[-2] + sumlist[-1]
		sumlist.append(newList)
		i += 1
	return sumlist

def rePlay(aList):
	while True:
		print fibonnaci(aList)
		playAgain = raw_input('play again? (y/n):  ')
		if playAgain != 'y':
			return 'goodbye' 

rePlay(a)