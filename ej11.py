number = int(input("Enter a number you would like to know whether is prime or not: "))


if number > 1:
    for div in range(2, number):
        if number % div == 0:
            print("%s is not a prime number" % number)
            break
    else:
        print("%s is a prime number" % number)
else:
    print("%s is not a prime number" % number)
