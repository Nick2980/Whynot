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
Dst.get_subjects()

#%%
