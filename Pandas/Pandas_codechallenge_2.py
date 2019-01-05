"""
code challenge
Continue with Titanic data set.
Another variable that could influence survival is age; since it's probable that 
children were saved first.
You can test this by creating a new column with a categorical variable Child. 
Child will take the value 1 in cases where age is less than 18, and a value of 0 in cases where age is greater than or equal to 18.

To add this new variable you need to do two things
1.     create a new column, and
2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
        Import the titanic_training set.
        Set the values of Child to 1 is the passenger's age is less than 18 years.
        Then assign the value 0 to observations where the passenger is greater than or equal to 18 years in the new Child column.
        Compare the normalized survival rates for those who are <18 and those who are older. Use code similar to what you had in the previous exercise.)
"""

import pandas as pd
import numpy as np
df = pd.read_csv("training_titanic.csv")

#filling nan values with mean vale of age
df['Age']=df['Age'].fillna(df['Age'].mean())

#To fill child column based on age
df['child'] = np.where(df['Age']>=18,0,1)

print("survival rates for those who are <18:",df["Survived"][df["child"]==1].value_counts(normalize=True)[1])
print("survival rates for those who are >18:",df["Survived"][df["child"]==0].value_counts(normalize=True)[1])