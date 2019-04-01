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
print(present_value(0.01))


