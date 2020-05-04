# Method 1: remove duplicates by converting
# list to a dictonary and then back to list


def remove():
    a = [1, 1, 5, 0, 6, 3, 5, 0]
    b = list(dict.fromkeys(a))
    return b


print(remove())

# Method 2: creates a function that appends the element
# in a to b, only if the element is not already in b
a = [1, 1, 5, 0, 6, 3, 5, 0]
b = []


def duplicates():
    for element in a:
        if element not in b:
            b.append(element)
    return b


print(duplicates())

# Method 2: using sets
a = [1, 1, 5, 0, 6, 3, 5, 0]


def delete(a):
    return list(set(a))


print(delete(a))
