#%%
# Import of pandas and numpy for work and analysis on lists and arrays
import pandas as pd
import numpy as np

#import custom present_value function
from present_value_function import present_value
#%%
# import of matplot for making graphs later on in the analysis
import matplotlib.pyplot as plt

#%%
#load rates from excel
rates = pd.read_excel('Morgagebond_rates.xlsx')

#%%
#add column to rates with the present_value of a 30-year annuity
rates['PV_Long_rates'] = present_value(rates['Long_rates'])

#calculation index value of pv column. Base year 2006
#for PV_Long_rates in enumerate(rates) 
#    index = 100
#    index = value 

print(rates)

#plt.scatter
#plt.show()