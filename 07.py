#list comprehensions

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

oldList = []

#the older way to type out the procedure
for num in a:
	if num%2 == 0:
		oldList.append(num)


#list comprehension, lines of code put into 1
#the append code is 
newList = [num for num in a if num%2 == 0]


if oldList == newList:
	print "List comprehension worked"
	print newList
