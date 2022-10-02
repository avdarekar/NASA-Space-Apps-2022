#!/usr/bin/env python
# coding: utf-8

# ## Selecting a Source ID from List

# In[44]:


# import libraries
from tkinter import *
import pandas as pd


# In[45]:


#get sourceids
def readGaiaData(path, cols): 
    return pd.read_csv(path, usecols = cols)

data = readGaiaData('/Users/adarekar/Downloads/GaiaUnivModel1.csv', cols = ['source_id', 'radius'])
source_id = list(data['source_id'])[:50]
radius = list(data['radius'])[:50]


# In[46]:


# create object
root = Tk()
root.geometry( "200x200" )

def show():
    label.config( text = clicked.get() )
  
# dropdown menu options
options = source_id
  
clicked = StringVar()
clicked.set("Select Source ID")
  
# Create dropdown box
drop = OptionMenu( root , clicked , *options )
drop.pack()
  
root.mainloop()


# In[ ]:




