def fibonacci():
    numbersToGenerate = int(input("Enter how many fibonacci numbers you want to generate: "))
    i = 1
    if numbersToGenerate == 0:
        sequence = []
    elif numbersToGenerate == 1:
        sequence = [1]
    elif numbersToGenerate == 2:
        sequence = [1, 1]
    elif numbersToGenerate > 2:
        sequence = [1, 1]
        while i < (numbersToGenerate - 1):
            sequence.append(sequence[i] + sequence[i-1])
            i += 1

    return sequence


print(fibonacci())
