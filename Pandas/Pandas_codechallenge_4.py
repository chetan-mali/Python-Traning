"""
Code Challenge on pandas:
    
In 2011, URL shortening service Bitly partnered with the US government website
USA.gov to provide a feed of anonymous data gathered from users who shorten links
ending with .gov or .mil. In 2011, a live feed as well as hourly snapshots were available
as downloadable text files. This service is shut down at the time of this writing (2017),
but we preserved one of the data files.
In the case of the hourly snapshots, each line in each file contains a common form of
web data known as JSON. (Use example.txt file from Resources)

    *Replace the 'nan' values with 'Mising' and ' ' values with 'Unknown' keywords
    *Print top 10 most frequent time-zones from the Dataset i.e. 'tz', with and without Pandas
    *Count the number of occurrence for each time-zone
    *Plot a bar Graph to show the frequency of top 10 time-zones (using Seaborn)
    *From field 'a' which contains browser information and separate out browser 
     capability(i.e. the first token in the string eg. Mozilla/5.0)
    *Count the number of occurrence for separated browser capability field 
     and plot bar graph for top 5 values (using Seaborn)
    *Add a new Column as 'os' in the dataset, separate users by 'Windows' for the 
     values in  browser information column i.e. 'a' that contains "Windows" and "Not Windows" 
     for those who don't
"""
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np
#creating dataframe form json data
df = pd.read_json("bitly-usagov-example.txt",lines=True)

#filling nan value with Mising
df = df.fillna("Mising")
#replacing empty value with Unknown
df = df.replace(r'^\s*$',"Unknown", regex=True)

#10 most frequent time-zones from the Dataset using pandas
print(df["tz"].value_counts().head(10))
#10 most frequent time-zones from the Dataset without pandas
dic={}
for i in df["tz"]:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1
dic=sorted([(value,key) for (key,value) in dic.items()],reverse=True)
print(dic[0:10])

#Counting the number of occurrence for each time-zone
print(df["tz"].value_counts())

#bar Graph to show the frequency of top 10 time-zones
ax = sns.barplot(df["tz"].value_counts().head(10).index,df["tz"].value_counts().head(10))
plt.show()

#the number of occurrence for separated browser capability field
f=df["a"].str.extractall(r'^([A-Za-z/\.0-9]+)')
f.index=range(3560)
df["Browser"]=f
print("occurrence browser",df["Browser"].value_counts())

ax = sns.barplot(df["Browser"].value_counts().head(5).index,df["Browser"].value_counts().head(5))
plt.show()

k=df["a"].str.find("Windows")
df["os"]=np.where(k==-1,'Not Windows','Windows')
