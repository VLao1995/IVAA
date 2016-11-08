import pandas as pd #import pandas (for Matrix)
from collections import Counter

csv_data = pd.read_csv("complete_food.csv", sep=",") #read the csv file
csv_data_df = pd.DataFrame(csv_data) #convert the csv into pandas dataframe

"""""
# Select and isolate certain rows and columns
csv_data_df.iloc[1, 2]

# Select the rows in which "British" is Yes
print(csv_data_df[~(csv_data_df['British'] > 0)])

#Create a new csv for every while Loop Trial, using this we can create a new column
print(csv_data_df.append(csv_data_df[csv_data_df['British'] > 0 ]))

# The concept of the while loop for our algorithm
List = [3,4,5]
Num = 6
while Num < 10:
    List.append(Num)
    Num = Num + 1

print(List)

"""""

