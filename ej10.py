import random
# #Prints a list (c) with elements shared between a and b
a = random.sample(range(20), 5)
b = random.sample(range(20), 5)
c = [num for num in a for numy in b if num == numy]
c = list(set(c))
print(c)
#Alternative way

a = random.sample(range(20), 5)
b = random.sample(range(20), 5)
c = [num for num in a if num in b]
c = list(set(c))
print(c)
