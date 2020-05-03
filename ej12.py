import random
a = random.sample(range(20), 4)
b = []


def first_and_last():
    for item in a:
        b.append((a[0]))
        b.append((a[-1]))
        print(b)
        break


first_and_last()
