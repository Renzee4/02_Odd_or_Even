import random

def makeList():
	newList = []
	i = 0
	while i < 10:
		num = random.randint(1, 10)
		newList.append(num)
		i += 1
	return newList

def count():
	aList = []
	someList = makeList()
	print someList
	for elem in someList:
		if someList.count(elem) == 1:
			aList.append(elem)
	return aList


print count()