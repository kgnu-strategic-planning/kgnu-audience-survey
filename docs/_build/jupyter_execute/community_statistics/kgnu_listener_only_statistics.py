#!/usr/bin/env python
# coding: utf-8

# # KGNU Listeners only
# 
# (Those who enjoy listening to KGNU but haven't financially contributed or become a KGNU *Volunteer* yet)

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import MaxNLocator
from IPython.display import display, Markdown


# In[2]:


df = pd.read_excel('KGNU-Member-Data-06.14.22.xlsx', sheet_name='English')
df_contributors = df[df['Ever_made_a_financial_contribution_to_KGNU?'] == 'Yes']
df_non_contributors = df[df['Ever_made_a_financial_contribution_to_KGNU?'] == 'No']
#print(len(df))
#print(len(df_contributors))
#print(len(df_non_contributors))


# ## By Age Groups

# In[3]:


df = pd.read_excel('KGNU-Member-Data-06.14.22.xlsx', sheet_name='English')
df = df[df.Age.notna()]
df['Age'] = df['Age'].astype('int')

df_listeners_only = df[(df['Ever_made_a_financial_contribution_to_KGNU?'] == 'No') & (df['Ever_been_a_KGNU_volunteer?'] == 'No')]

a = [1, 2, 3, 4, 5]
b = ['0-18', '19-30', '31-45', '46-65', '66+']
ages = df_listeners_only['Age'].map(dict(zip(a, b)))

ages.value_counts().plot.bar(rot=90)
plt.title('Listeners-only by Age Group')

axes = plt.gca()       
ya = axes.get_yaxis()
ya.set_major_locator(MaxNLocator(integer=True))

plt.xlabel('Age Groups')
plt.ylabel('Number of Listeners')

plt.show()

print(f'Respondents: {len(df)}')
print(f'Listeners within those Respondents: {len(df_listeners_only)}')


# ## By Counties

# In[4]:


df = pd.read_excel('KGNU-Member-Data-06.14.22.xlsx', sheet_name='English')
df = df[df.County.notna()]
df_listeners_only = df[(df['Ever_made_a_financial_contribution_to_KGNU?'] == 'No') & (df['Ever_been_a_KGNU_volunteer?'] == 'No')]

a = df_listeners_only.County.unique().tolist()
b = ['Denver','Boulder','Jefferson','Arapahoe','All Other Counties','Broomfield','All Other Counties','All Other Counties','Adams','All Other Counties','All Other Counties',\
     'Larimer','All Other Counties','Douglas','All Other Counties','All Other Counties','All Other Counties','All Other Counties','All Other Counties','All Other Counties',\
     'All Other Counties','All Other Counties','Weld','All Other Counties','All Other Counties','All Other Counties','All Other Counties','All Other Counties',\
     'All Other Counties','All Other Counties','All Other Counties','All Other Counties']

counties = df_listeners_only['County'].map(dict(zip(a, b)))

counties.value_counts().plot.bar(rot=90)
plt.title('Listeners-only by County')

axes = plt.gca()       
ya = axes.get_yaxis()
ya.set_major_locator(MaxNLocator(integer=True))

plt.xlabel('Counties')
plt.ylabel('Number of Listeners')

plt.show()

print(f'Respondents: {len(df)}')
print(f'Listeners within those Respondents: {len(df_listeners_only)}')


# ## By Self-Identified Race Categories

# In[5]:


df = pd.read_excel('KGNU-Member-Data-06.14.22.xlsx', sheet_name='English')
df = df[df.You_Are.notna()]
df_listeners_only = df[(df['Ever_made_a_financial_contribution_to_KGNU?'] == 'No') & (df['Ever_been_a_KGNU_volunteer?'] == 'No')]

df_listeners_only['You_Are'].value_counts().plot.bar(rot=90)
plt.title('Listeners-only by Self-Identified Race')

axes = plt.gca()       
ya = axes.get_yaxis()
ya.set_major_locator(MaxNLocator(integer=True))

plt.xlabel('Race Categories')
plt.ylabel('Number of Listeners')

plt.show()

print(f'Respondents: {len(df)}')
print(f'Listeners within those Respondents: {len(df_listeners_only)}')


# ## By Household Income

# In[6]:


df = pd.read_excel('KGNU-Member-Data-06.14.22.xlsx', sheet_name='English')
df = df[df.Household_Income.notna()]
df_hhi_1 = df[df['Household_Income'] == 13]
##print(len(df))
##print(len(df_hhi_1))


# In[7]:


df = pd.read_excel('KGNU-Member-Data-06.14.22.xlsx', sheet_name='English')
df = df[df.Household_Income.notna()]
df['Household_Income'] = df['Household_Income'].astype('int')

df_listeners_only = df[(df['Ever_made_a_financial_contribution_to_KGNU?'] == 'No') & (df['Ever_been_a_KGNU_volunteer?'] == 'No')]

a = [1, 2, 3, 4, 7, 13]
b = ['Less than $25k', '\$25k - $49k', '\$50k - $99k', '\$100k - $199k', ' $200k +', 'Prefer not to answer']
household_incomes = df_listeners_only['Household_Income'].map(dict(zip(a, b)))

household_incomes.value_counts().plot.bar(rot=90)
plt.title('Listeners-only by Household Income')

axes = plt.gca()       
xa = axes.get_yaxis()
ya.set_major_locator(MaxNLocator(integer=True))

plt.xlabel('Household Income Categories')
plt.ylabel('Number of Listeners')

plt.show()

print(f'Respondents: {len(df)}')
print(f'Listeners within those Respondents: {len(df_listeners_only)}')

