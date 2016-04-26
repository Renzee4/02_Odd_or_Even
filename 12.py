import random

randomList = random.sample(range(1, 20), 10)

def newList(someList):
	replaced = []
	replaced.extend([someList[0], someList[len(someList)-1]])
	print replaced

print randomList
newList(randomList)

