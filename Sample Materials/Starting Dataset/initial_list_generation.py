import random as rand

# Generates an ordered list that goes from 0 to 100000
lst = list(range(100001))

# Shuffles the order of all elements in this list
rand.shuffle(lst)

# Writes this shuffled list into a txt file, with each element as a new line
file = open("randomized_list_int.txt", "w")

for element in lst:
    file.write(str(element) + "\n")
file.close()
