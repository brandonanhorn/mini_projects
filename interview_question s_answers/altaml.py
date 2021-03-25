import pandas as pd

'''IMPORTANT: click on "Compile & Run" to generate an output to the written code
ONLY this will generate scores for your code!
Also this will help you to check correctness of your code against test cases'''

import numpy as np
import pandas as pd

#dataset is given below
dataset = [[101,31,"M",310,518,677,1505],
           [102,53,"M",356,548,629,1520],
           [106,26,"M",387,605,553,1545],
           [113,15,"U",301,508,524,1333],
           [115,21,"U",376,627,647,1638],
           [120,10,"M",289,482,682,1453],
           [121,22,"U",402,674,518,1594],
           [110,47,"M",319,536,518,1594],
           [122,13,"U",297,502,590,1403],
           [130,19,"U",355,583,684,1622],
           [131,72,"U",265,471,544,1280],
           [133,65,"M",286,496,677,1460],
           [125,16,"M",347,568,518,1433],
           [141,28,"M",416,688,561,1665]
          ]

from pandas import DataFrame
## Converting the list to a Data Frame
df = DataFrame(dataset,columns=["Patient ID", "Age", "Marital Status", "Breakfast Calorie", "Lunch Calorie", "Dinner Calorie", "Total Calorie"])
## Printing first item in list to see if it worked
df.head(1)
## Changing the Total Calorie column
df["Total Calorie"] = df["Breakfast Calorie"] + df["Lunch Calorie"] + df["Dinner Calorie"]
## Showing the people who under 18 and married
df
df[(df["Marital Status"] == "M") & (df["Age"] < 18)]
## Creating new df with bad data
df.loc[(df["Marital Status"] == "M") & (df["Age"] < 18)].replace("M", "U")
## Replacing Married with Unmarried
df_1["Marital Status"] = df_1["Marital Status"].replace("M", "U")
df_1
df


df.loc[(df["Marital Status"] == "M") & (df["Age"] < 18),"Marital Status"]="U"
df

df.columns[2]
