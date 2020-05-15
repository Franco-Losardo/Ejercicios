a = [1, 3, 5, 30, 42, 43, 500]
b = 89

def in_list():
    for number in a:
        if number == b:
            return True
    return False
        
print(in_list())


# Using binary search

def find(l, number):
    minim = 0
    maxim = len(l) - 1
    while minim <= maxim:
        cur = int((minim + maxim) / 2)

        if l[cur] == number:
            return True
        elif l[cur] > number:
            maxim = cur - 1
        else:
            minim = cur + 1
    return False


print(find(a, b))


