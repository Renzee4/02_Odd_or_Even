#

num = input('Enter a number: ')
num = int(num)

def number(num):
	if num%2 == 0:
		return "This number is an even number, hooray"
	else:
		return "This number is an odd number for an odd person. LIKE YOU"

print number(num)

