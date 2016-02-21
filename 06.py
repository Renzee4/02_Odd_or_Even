string = raw_input("Type a palindrome: ")


if string == string[::-1]:
	print "Correct! " + string + " spelled backwards is " + string
else:
	print "NOPE, that's not a palindrome.. sorry"


