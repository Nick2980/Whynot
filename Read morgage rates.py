#%%
# Import of pandas and numpy for work and analysis on lists and arrays
import pandas as pd
import numpy as np
#%%
# import of matplot for making graphs later on in the analysis
import matplotlib.pyplot as plt

#%%
#load rates from excel
rates = pd.read_excel('Morgagebond_rates.xlsx')

#%%
print(rates)

