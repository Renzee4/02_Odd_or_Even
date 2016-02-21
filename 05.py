import random


#random list generator, different lengths 
a = random.sample(range(1, 20), 5)
b = random.sample(range(1, 20), 8)

print "This is list a: ", a
print "This is list b: ", b
print " "


c = []

for elem in a:
	if elem in b:
		c.append(elem)
print "Common numbers between the two lists: "
print c