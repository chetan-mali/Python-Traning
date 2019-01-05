"""
Code challenge
Import the training set “training_titanic.csv ” .

It’s a real-world data containing the details of titanic ships passengers list.
Now Answer the following:
        How many people in the given training set survived the disaster with the 
        Titanic and how many of them died? 
        
        Calculate and print the survival rates as proportions (percentage) 
        by setting the normalize argument to True.
        
        Repeat the same calculations but on subsets of survivals based on Sex:
            Males that survived vs males that passed away
            Females that survived vs Females that passed away
"""

import pandas as pd

df = pd.read_csv("training_titanic.csv")
print("Total Survived Passenger:",df["Survived"].value_counts()[1])
print("Survival rates :",df["Survived"].value_counts(normalize=True)[1])

print("Males that passed away:",df["Survived"][df["Sex"]=="male"].value_counts()[0])
print("Males that survived:",df["Survived"][df["Sex"]=="male"].value_counts()[1])

print("Females that passed away:",df["Survived"][df["Sex"]=="female"].value_counts()[0])
print("Females that survived:",df["Survived"][df["Sex"]=="female"].value_counts()[1])