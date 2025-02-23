#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy  as np
import pandas as pd


# In[5]:


df=pd.read_csv('UK-HPI-full-file-2024-01.csv')


# In[6]:


df


# In[7]:


df.info()


# In[8]:


df.head()



# In[9]:


df.shape


# In[10]:


print(df.isnull().sum())
 


# In[12]:


df1 = df.dropna() 


# In[13]:


df1


# In[14]:


df2 = df1.drop_duplicates()


# In[15]:


df2


# In[ ]:




