#%%
# Import of pandas and numpy for work and analysis on lists and arrays
import pandas as pd
import numpy as np
#%%
# import of matplot for making graphs later on in the analysis
import matplotlib.pyplot as plt

#%%
##Present value function
def present_value(rate):
    """ The present value of a annuity. 
    Calulates the present value of a yearly payment of 1 kr. paid in 30 years at rate x.
    Args:
        rate (float): the rate
        
    Returns:
        present value of 1 kr. in 30 years at rate x
    """
    try:
        return (1 - (1 + rate)**-30)/rate 

    except:
        print('Error: Check input')

#%%
#load rates from excel
rates = pd.read_excel('Morgagebond_rates.xlsx')

#%%
#line = rates.plt.plot
print(rates['Long_rates'])

#%%
present_value_list = present_value(rates['Long_rates'])

rates['pv'] = present_value(rates['Long_rates'])

print(rates)




#plt.scatter
#plt.show()