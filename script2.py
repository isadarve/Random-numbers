# Author: Isabel Adarve

# Importing libraries

import pandas as pd
import matplotlib.pyplot as plt

# Importing the JSON as a Dataframe

df = pd.read_json ('random_number_list.json', orient='columns')

df = pd.DataFrame(df['numbers'].value_counts())
df.reset_index(drop=False, inplace = True)
df.rename(columns={'index':'numbers', 'numbers': 'frequency'}, inplace=True)
df.sort_values(by='numbers', inplace = True)
df.reset_index(drop=True, inplace=True)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0,0,1,1])
ax.bar(df['numbers'],df['frequency'])
plt.show()