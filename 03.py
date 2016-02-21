import random

print " " 
print "LET'S PLAY A GAME"

pick_a_range = input("Pick a range of numbers: ")
pick_a_range = int(pick_a_range)

sample_N = input("How many numbers in list to display: ")
sample_N = int(sample_N)

aList = random.sample(range(pick_a_range), sample_N)

print "Here is your list of numbers :) "
print aList

numToRemove = input("Up to what value do you want to see in this list?: ")
numToRemove = int(numToRemove)

bList = []

for num in aList:
	if num < numToRemove:
		bList.append(num)

print bList
print "----The End---"
