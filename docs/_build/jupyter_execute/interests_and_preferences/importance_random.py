#!/usr/bin/env python
# coding: utf-8

# # Importance Preferences - Random
# 
# In this section we look for correlations between what respondents consider 'Important' categories of programming and examine which Media Outlets they use on a regular basis to obtain such programming.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import MaxNLocator
from IPython.display import display, Markdown
from functions import *


# In[2]:


df = pd.read_excel('Client Data English-07.15.22.xlsx', sheet_name='English') 


# ## Local News

# In[3]:


create_regular_outlet_users_by_importance_preference(df, 'Local_News_Importance', 'Local News')


# ## Weather Reports

# In[4]:


create_regular_outlet_users_by_importance_preference(df, 'Weather_Importance', 'Weather Reports')


# ## Traffic Reports

# In[5]:


create_regular_outlet_users_by_importance_preference(df, 'Traffic_Reports_Importance', 'Traffic Reports')


# ## Music Programming

# In[6]:


create_regular_outlet_users_by_importance_preference(df, 'Music_Programming_Importance', 'Music Programming')


# ## National News

# In[7]:


create_regular_outlet_users_by_importance_preference(df, 'National_news_Importance', 'National News')


# ## International News

# In[8]:


create_regular_outlet_users_by_importance_preference(df, 'International_news_Importance', 'International News')


# ## Breaking News Bulletins

# In[9]:


create_regular_outlet_users_by_importance_preference(df, 'Breaking_news_bulletins_Importance', 'Breaking News Bulletins')


# ## Community Events

# In[10]:


create_regular_outlet_users_by_importance_preference(df, 'Community_Events_Importance', 'Community Events')


# ## Local Government Coverage

# In[11]:


create_regular_outlet_users_by_importance_preference(df, 'Local_Government_Coverage_Importance', 'Local Government Coverage')


# ## Political Analysis

# In[12]:


create_regular_outlet_users_by_importance_preference(df, 'Political_Analysis_Importance', 'Political Analysis')


# ## Local Public Affairs

# In[13]:


create_regular_outlet_users_by_importance_preference(df, 'Local_Public_Affairs_Importance', 'Local Public Affairs')

