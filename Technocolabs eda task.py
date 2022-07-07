#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[5]:


loan=pd.read_csv('C:\\Users\\user\\Desktop\\prosperLoanData.csv')


# In[6]:


loan.head()


# In[10]:


loan.columns


# In[11]:


loan.info()


# In[12]:


loan.describe()


# In[13]:


loan.isnull().sum()


# In[15]:


[features for features in loan.columns if loan[features].isnull().sum()>0]


# In[16]:


sns.heatmap(loan.isnull(),cbar=False,cmap='viridis')


# In[18]:


loan.dropna(subset = ["CreditGrade"], axis = 0, inplace = True)
loan["CreditGrade"].isnull().count()
loan.reset_index(drop=True, inplace=True)
loan.head()


# In[20]:


loan.dtypes


# In[ ]:





# In[ ]:




