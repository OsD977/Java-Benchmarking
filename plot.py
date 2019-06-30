import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as stats
import pylab as pl

#y1 = pd.read_csv('0.csv', sep=',', usecols = [0],names=['Standard']).values
y2 = pd.read_csv('1.csv', sep=',', usecols = [0],names=['Standard']).values
y3 = pd.read_csv('2.csv', sep=',', usecols = [0],names=['Standard']).values
y4 = pd.read_csv('3.csv', sep=',', usecols = [0],names=['Standard']).values
y5 = pd.read_csv('4.csv', sep=',', usecols = [0],names=['Standard']).values


x = range(0,50)


#plt.plot(x,y1) 
plt.plot(x,y2) 
plt.plot(x,y3) 
plt.plot(x,y4) 
plt.plot(x,y5) 

plt.legend(['-XX:TieredStopAtLevel=1', '-XX:TieredStopAtLevel=2', 
            '-XX:TieredStopAtLevel=3', '-XX:TieredStopAtLevel=4'])


plt.xlabel('#Iterations')
plt.ylabel('ms/op')
plt.show()
