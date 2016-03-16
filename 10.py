import random

a = random.sample(range(1, 20), 10)
b = random.sample(range(1, 20), 18)

#a = [1, 1, 2, 3, 5, 8, 11, 11, 11, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print a
print b

old_c = [elem for elem in a if (elem in b)]
c = set([elem for elem in a if (elem in b)])

print old_c
print c

d = [elem for elem in set(a) if (elem in b)]
print d
