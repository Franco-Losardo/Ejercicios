with open('happyNumbers.txt', 'r') as f, open('primeNumbers.txt', 'r') as f2:
    happy_numbers = f.read()
    prime_numbers = f2.read()
    # Converts file to list
    formatted_happys = happy_numbers.split()
    formatted_primes = prime_numbers.split()

    overlapping = []
    with open ("numbers overlapping.txt", "w") as file:
        for number in formatted_happys:
            if number in formatted_primes:
                overlapping.append(int(number))

print(overlapping)