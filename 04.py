## intro
print " "
print "LETS PLAY A GAME :]"
## begin code


number = int(input("Put in a number: "))

#lists are created by user
aList = range(1, number)
bList = []


for elem in aList:
	if number % elem == 0:
		divided = number / elem
		bList.append(divided)


print "Divisors: "
print bList
