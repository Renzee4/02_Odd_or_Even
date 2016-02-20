#
#User input numbers
num = input('Enter a number: ')
num = int(num)

check = input('Enter another number: ')
check = int(check)

print " "

#divisible by 2
if num%2 == 0:
	print "This number is an even number, hooray"
else:
	print "This number is an odd number for an odd person. LIKE YOU"

#divisible by 4
if num%4 == 0:
	print "This number is a multiple of 4"
else:
	print "Not a multiple of 4"

#users' input of two numbers divided EVENLY
if num%check == 0:
	print "This number divided EVENLY, you graduated prematurely"
else: 
	print "Nope, didn't divide evenly, sorry Felicia"


print " "
print "---The End---"
