"""
Created on Wed Dec 26 14:37:27 2018
@author: chetan mali
"""
"""
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""
import numpy as np

num = input("Enter: ").split(" ")
#a.reverse()
num_arr = np.array(num,int)
print(np.reshape(num_arr, (3,3)))

"""
  Name: 
    E-commerce Data Exploration
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Execute the code snippet below.
          import numpy as np
          import matplotlib.pyplot as plt
          incomes = np.random.normal(100.0, 20.0, 10000)
          print (incomes)
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers       
  Hint: 
    outlier is an observation that lies an abnormal distance from other values 
    in a random sample from a population) to it to see their effect.
"""
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0,20.0,10000)
plt.hist(incomes, 50)
plt.show()

print("Mean:",np.mean(incomes))
print("Median:",np.median(incomes))

"""
  Name: 
    Normally Distributed Random Data
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(150.0,20.0,1000)
plt.hist(incomes, 100)
plt.show()

print("Standard Devation:",np.std(incomes))
print("Variance:",np.var(incomes))

"""
  Name: 
    Random Data
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.

  Solution:
import numpy as np
a = np.random.randint(5,15,40)
d = {}
fin = []

for i in a:
    d[i] = d.get(i,0)+1

for i in d.items():
    j,k = i
    i = k,j
    fin.append(i)

fin.sort()
freq,num = fin[-1]

Or optional Method

num = np.bincount(a).argmax()


print ("The most Frequent Number is",num)
    
"""
import numpy as np

arr = np.random.randint(5,15,40)
counts = np.bincount(arr)
print (np.argmax(counts))
