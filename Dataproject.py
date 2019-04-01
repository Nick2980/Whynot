#%%
# Import of pandas and numpy for work and analysis on lists and arrays
import pandas as pd
import numpy as np
#%%
# import of matplot for making graphs later on in the analysis
import matplotlib.pyplot as plt
#%%
# import of dst API functions. Note: requires installation of pip install git+https://github.com/elben10/pydst in terminal(mac)/cmd(windows)
import pydst
Dst = pydst.Dst(lang='da')

#%%
# Fetching variables for the consumer price index in dst
forpris_vars = Dst.get_variables(table_id='PRIS112')
forpris_vars

#%%
# Fetching data for the yearly average consumer price index with 2005=100
forprisindex = Dst.get_data(table_id = 'PRIS112', variables={'HOVED':['1005'], 'tid':['*']})

forprisindex.sample(10)
#%%
# Fetching variables for the property price index in dst
ejpris_vars = Dst.get_variables(table_id='EJ55')
ejpris_vars
#%%
ejpris_vars['values'][1][:10]
ejpris_vars['values'][2][:10]
ejpris_vars['values'][3][:]

#%%
TIDID=ejpris_vars['values'][3][:]
K4=TIDID[3::4]
#%%
K4id = []
for row in K4:
    K4id.append(row['id'])
K4id
#%%
K4input=''
for year in K4id:
    K4input +=  year + ','
K4input
#%%
ejprisindex = Dst.get_data(table_id = 'EJ55', variables={'OMRÅDE':['01'], 'EJENDOMSKATE':['2103'], 'TAL':['100'], 'Tid':[K4input]})
ejprisindex

