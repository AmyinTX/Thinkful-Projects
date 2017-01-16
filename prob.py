# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 11:06:12 2017

@author: amybrown
"""

#for use with jupyter notebook, must make paths to modules explicit
import sys

sys.path.append('/Users/amybrown/anaconda3/lib/python3.5/site-packages/numpy/__init__.py')
import numpy as np

sys.path.append('/Users/amybrown/anaconda3/lib/python3.5/site-packages/scipy/stats/__init__.py')
import scipy.stats as stats


sys.path.append('/Users/amybrown/anaconda3/lib/python3.5/site-packages/matplotlib/pyplot.py')
import matplotlib.pyplot as plt

sys.path.append('/Users/amybrown/anaconda3/lib/python3.5/collections/__init__.py')
import collections



#### start with discrete data in first example ####
testlist = [1, 4, 5, 6, 9, 9, 9]

c = collections.Counter(testlist)
print(c)
count_sum = sum(c.values())
for k, v in c.items():
    print('The frequency of number ' + str(k) + ' is ' + str(float(v) / count_sum)) # obtains frequency
    
plt.boxplot(testlist) # creates boxplot
plt.show()
plt.hist(testlist, histtype='bar') # creates a histogram
testlist_graph = stats.probplot(testlist, dist='norm', plot=plt) # creates a QQ plot

### next, use discrete data from the boxplot example ###

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

xcount = collections.Counter(x)
print(x)
x_sum = sum(xcount.values())
for k, v in xcount.items():
    print('The frequency of number ' + str(k) + ' is ' + str(float(v) / x_sum))
    
plt.boxplot(x)
plt.hist(x, histtype='bar')
x_qq = stats.probplot(x, dist='norm', plot=plt)


### finally, use normally and uniformly distributed data from continuous data example ###

test_data1 = np.random.normal(size=1000)   # create normally distributed data


td1 = collections.Counter(test_data1)
cs_td1 = sum(td1.values())
for k, v in td1.items():
    print('The frequency of number ' + str(k) + ' is ' + str(float(v) / cs_td1))
    
plt.boxplot(test_data1)
plt.hist(test_data1, histtype='bar')
graph1 = stats.probplot(test_data1, dist='norm', plot=plt)



test_data2 = np.random.uniform(size=1000)   # create uniformally distributed data

td2 = collections.Counter(test_data2)
cs_td2 = sum(td2.values())
for k, v in td2.items():
    print('The frequency of number ' + str(k) + ' is ' + str(float(v) / cs_td1))
    
plt.boxplot(test_data2)
plt.hist(test_data2, histtype='bar')
graph2 = stats.probplot(test_data2, dist='norm', plot=plt)


