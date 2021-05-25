# Author: Isabel Adarve

# Importing libraries

import random
import json

# Creating a list with 1000 random numbers between 0 and 100

L = []
for elem in range(0,1000):
    L.append(randrange(101))

# Creating a dictionary using the list

dicts = {'numbers' : L}

# Saving the dictionary in a JSON file

with open('random_number_list.json', 'w') as fp:
    json.dump(dicts, fp)