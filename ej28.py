def largest(a, b, c):
    if a > b and a > c:
        return "The largest number is {}".format(a)
    elif b > c:
        return "The largest number is {}".format(b)
    else:
        return "The largest number is {}".format(c)

print(largest(3,11,132))
