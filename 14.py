import random

def makeList():
	newList = []
	i = 0
	while i < 10:
		num = random.randint(1, 10)
		newList.append(num)
		i += 1
	print newList
	return newList

def remove_dups():
	noDupsList = set(makeList())
	return noDupsList

print remove_dups()