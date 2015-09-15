# Learn Python - Lesson 1

# Import all libraries needed for this tutorial

# General syntax to import specific functions in a library:
# from (library) import (specific lbrary function)
from pandas import DataFrame, read_csv

# General syntax to import a library, but no functions:
# import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd # this is how I usually import pandas
import sys # only needed to dtermine Python version number

print "Python version " + sys.version
print "Pandas version " + pd.__version__


# CREATE DATA
# The initial set of baby names and birth rates
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = zip(names, births)
BabyDataSet

df = pd.DataFrame(data = BabyDataSet, columns = ['Names', 'Births'])
df

# WRITE TO CSV
df.to_csv('births1880.csv', index = False, header = False)


# GET DATA

Location = r'C:\Users\Craig\Documents\Python Scripts\Pandas\births1880.csv'
# the r before the file location escapes the whole string because of the slash
# the below line is how we read in a csv, but it freezes for me when header = None

#df = pd.read_csv(Location, header=None)
#df


# PREPARE DATA
# check data type of columns
df.dtypes

# check data type of births column
df.Births.dtype

# ANALYZE DATA
# find the most popular baby name (highest birth rate)
# method 1:
Sorted = df.sort(['Births'], ascending=False)
Sorted.head(1)

# method 2:
df['Births'].max()

# PRESENT DATA

# create graph
df['Births'].plot()

# maximum value in the data set
MaxValue = df['Births'].max()

# name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()]

# text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy = (1, MaxValue), xytext = (8, 0),
             xycoords = ('axes fraction', 'data'), textcoords = 'offset points')

print "The most popular name"
df[df['Births'] == df['Births'].max()]
