#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing libraries

import numpy as np
import pandas as pd
import warnings
warnings.simplefilter("ignore")


# In[2]:


df=pd.read_excel("C:/Users/Mayank/Documents/Analytics/B&K/file.xlsx")


# In[3]:


df.info()


# In[4]:


df.duplicated(['first_name'], keep='first').sum()


# In[5]:


data_frame=df.drop_duplicates(['first_name'],keep='first')
data_frame


# In[ ]:




