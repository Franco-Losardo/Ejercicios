with open('file.txt', 'r') as open_file:
    all_text = open_file.read()

formatted_file = all_text.split()
Darth = 0
Lea = 0
Luke = 0
        
for name in formatted_file:
    if name == "Darth":
        Darth += 1
    elif name == "Lea":
        Lea += 1
    else:
        Luke += 1
print("There are {} Darths, {} Leas and {} Lukes".format(Darth, Lea, Luke))

# Script with long file

counter_dict = {}
with open('long_file.txt') as f:
	line = f.readline()
	while line:
		line = line[3:-26]
		if line in counter_dict:
			counter_dict[line] += 1
		else:
			counter_dict[line] = 1
		line = f.readline()

print(counter_dict)