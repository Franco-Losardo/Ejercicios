import random
# Method 1
with open('sowpods.txt', 'r') as open_file:
  random_word = list(open_file)
  print(random.choice(random_word).strip())

# Method 2
with open('sowpods.txt', 'r') as open_file:
    all_text = open_file.read()
    new_list = all_text.split()
    random_word = random.choice(new_list)
    print(random_word)

