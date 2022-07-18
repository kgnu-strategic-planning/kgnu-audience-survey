#!/usr/bin/env python
# coding: utf-8

# # Programming Preferences Rankings
# 
# In this section programming preferences are ranked in order of how important they were rated

# In[1]:


import pandas as pd
import numpy as npb
import matplotlib.pyplot as plt
from pylab import MaxNLocator
from IPython.display import display, Markdown
from functions import *


# In[2]:


df = pd.read_excel('KGNU-Member-Data-07.15.22.xlsx', sheet_name='English') 


# ## All Respondents

# In[3]:


create_ranked_table_of_importances(df, 'all_respondents', '', 'Filter: None')


# ## By Age

# ### Ages 0 - 18

# In[4]:


create_ranked_table_of_importances(df, 'Age', 1, 'Filter: Ages 0 - 18')


# ### Ages 19 - 30

# In[5]:


create_ranked_table_of_importances(df, 'Age', 2, 'Filter: Ages 19 - 30')


# ### Ages 31 - 45

# In[6]:


create_ranked_table_of_importances(df, 'Age', 3, 'Filter: Ages 31 - 45')


# ### Ages 46 - 65

# In[7]:


create_ranked_table_of_importances(df, 'Age', 4, 'Filter: Ages 46 - 65')


# ### Ages 66+

# In[8]:


create_ranked_table_of_importances(df, 'Age', 5, 'Filter: Ages 65+')


# ## By County

# ### Boulder County

# In[9]:


create_ranked_table_of_importances(df, 'County', 'Boulder', 'Filter: Boulder County')


# ### Denver County

# In[10]:


create_ranked_table_of_importances(df, 'County', 'Denver', 'Filter: Denver County')


# ### Jefferson County

# In[11]:


create_ranked_table_of_importances(df, 'County', 'Jefferson', 'Filter: Jefferson County')


# ### Arapahoe County

# In[12]:


create_ranked_table_of_importances(df, 'County', 'Arapahoe', 'Filter: Arapahoe County')


# ### Adams County

# In[13]:


create_ranked_table_of_importances(df, 'County', 'Adams', 'Filter: Adams County')


# ### Larimer County

# In[14]:


create_ranked_table_of_importances(df, 'County', 'Larimer', 'Filter: Larimer County')


# ### Weld County

# In[15]:


create_ranked_table_of_importances(df, 'County', 'Weld', 'Filter: Weld County')


# ### Douglas County

# In[16]:


create_ranked_table_of_importances(df, 'County', 'Douglas', 'Filter: Douglas County')


# ### Broomfield County

# In[17]:


create_ranked_table_of_importances(df, 'County', 'Broomfield', 'Filter: Broomfield County')


# ### All Other Counties

# In[18]:


create_ranked_table_of_importances(df, 'other_counties', '', 'Filter: All Other Counties')


# ## By Race

# ### Black or African American

# In[19]:


create_ranked_table_of_importances(df, 'You_Are', 'Black or African American', 'Filter: Black or African American')


# ### Hispanic, Latino, Chicano

# In[20]:


create_ranked_table_of_importances(df, 'You_Are', 'Hispanic, Latino/a/x, Chicano/a/x', 'Filter: Hispanic, Latino, Chicano')


# ### Middle Eastern or Arab

# In[21]:


create_ranked_table_of_importances(df, 'You_Are', 'Middle Eastern or Arab', 'Filter: Middle Eastern or Arab')


# ### Native American or Native Alaskan

# In[22]:


create_ranked_table_of_importances(df, 'You_Are', 'Native American or Native Alaskan', 'Filter: Native American or Native Alaskan')


# ### Native Hawaiian or Pacific Islander

# In[23]:


create_ranked_table_of_importances(df, 'You_Are', 'Native Hawaiian or Pacific Islander', 'Filter: Native Hawaiian or Pacific Islander')


# ### Prefer not to say

# In[24]:


create_ranked_table_of_importances(df, 'You_Are', 'Prefer not to say', 'Filter: Prefer not to say')


# ### Prefer to self identify

# In[25]:


create_ranked_table_of_importances(df, 'You_Are', 'Prefer to self identify:', 'Filter: Prefer to self identify')


# ### White

# In[26]:


create_ranked_table_of_importances(df, 'You_Are', 'White', 'Filter: White')


# In[ ]:




