#!/usr/bin/env python
# coding: utf-8

# # Ages 0 - 18

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import MaxNLocator
from IPython.display import display, Markdown
from functions import *


# In[2]:


df = pd.read_excel('KGNU-Member-Data-07.15.22.xlsx', sheet_name='English') 


# In[3]:


show_ratings_cols = df.columns.tolist()[111:191]
#show_ratings_cols


# In[4]:


filter_col = 'Age'
filter_col_val = 1
filter_col_val_display = 'Filter: Ages 0 - 18'


# ## Show Rankings

# In[5]:


create_ranked_table_of_shows(df, False, filter_col, filter_col_val, filter_col_val_display)


# ## Music Shows

# ### A Classic Monday

# In[6]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'A_Classic_Monday_Ratings')


# ### African Roots

# In[7]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'African_Roots_Ratings')


# ### Afternoon Sound Alternative

# In[8]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'ASA_Ratings')


# ### Blues Legacy

# In[9]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Blues_Legacy_Ratings')


# ### Corriente

# In[10]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Corriente_Ratings')


# ### Dub Palace

# In[11]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Dub_Palace_Ratings')


# ### Dusty Grooves

# In[12]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Dusty_Grooves_Ratings')


# ### Eclipse

# In[13]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Eclipse_Ratings')


# ### Electronic Air

# In[14]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Electronic_Air_Ratings')


# ### eTown

# In[15]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'E_Town_Ratings')


# ### Gospel Chime

# In[16]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Gospel_Chime_Ratings')


# ### Grateful Dead

# In[17]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Grateful_Dead_Ratings')


# ### Hwy 322

# In[18]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'HWY_322_Ratings')


# ### Honky Tonk Heroes

# In[19]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'HTH_Ratings')


# ### Jazz Lives

# In[20]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Jazz_Lives_Ratings')


# ### Kaberet

# In[21]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Kaberet_Ratings')


# ### Morning Sound Alternative

# In[22]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'MSA_Ratings')


# ### Musica Mundi

# In[23]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Musica_Mundi_Ratings')


# ### Old Grass Gnu Grass

# In[24]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'OGGG_Ratings')


# ### The Present Edge

# In[25]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Present_Edge_Ratings')


# ### Ragtime America

# In[26]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Ragtime_America_Ratings')


# ### Reggae Bloodlines

# In[27]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Reggae_Bloodlines_Ratings')


# ### Reggae Transfusions

# In[28]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Reggae_Transfusions_Ratings')


# ### Restless Mornings

# In[29]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Restless_Mornings_Ratings')


# ### Roots and Branches

# In[30]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Roots_and_Branches_Ratings')


# ### Roots of Jazz

# In[31]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Roots_of_Jazz_Ratings')


# ### Seolta Gael

# In[32]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Seolta_Gael_Ratings')


# ### Sleepless Nights

# In[33]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Sleepless_Nights_Ratings')


# ### Smash It Back

# In[34]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Smash_It_Back_Ratings')


# ### SoundLab

# In[35]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Soundlab_Ratings')


# ### Swing Shift

# In[36]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Swing_Shift_Ratings')


# ### Terrasonic

# In[37]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Terrasonic_Ratings')


# ### The Heavy Set

# In[38]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'The_Heavy_Set_Ratings')


# ### The Opera Box

# In[39]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'The_Opera_Box_Ratings')


# ### Under the Floorboards

# In[40]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Under_the_Floorboards_Ratings')


# ## News Shows

# ### A Public Affairs

# In[41]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'A_Public_Affair_Ratings')


# ### Alan Watts

# In[42]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Alan_Watts_Ratings')


# ### Alternative Radio

# In[43]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Alternative_Radio_Ratings')


# ### BBC News Hour

# In[44]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'BBC_News_Hour_Ratings')


# ### BBC The Newsroom

# In[45]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'BBC_The_Newsroom_Ratings')


# ### Between the Lines

# In[46]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Between_the_Lines_Ratings')


# ### Bioneers

# In[47]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Bioneers_Ratings')


# ### Black Talk

# In[48]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Black_Talk_Ratings')


# ### Colorado Chinese Radio Network

# In[49]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Col_Chinese_Radio_Network_Ratings')


# ### Connections

# In[50]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Connections_Ratings')


# ### Counterspin

# In[51]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Counterspin_Ratings')


# ### Democracy Now

# In[52]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Democracy_Now_Ratings')


# ### Economic Update

# In[53]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Economic_Update_Ratings')


# ### Hemispheres

# In[54]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Hemispheres_Ratings')


# ### How on Earth

# In[55]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'How_on_Earth_Ratings')


# ### Indian Voices

# In[56]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Indian_Voices_Ratings')


# ### It's the Economy

# In[57]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Its_The_Economy_Ratings')


# ### Jim Hightower

# In[58]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Jim_Hightower_Ratings')


# ### La Lucha Sigue

# In[59]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'La_Lucha_Sigue_Ratings')


# ### Labor Exchange

# In[60]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Labor_Exchange_Ratings')


# ### Linea Abierta

# In[61]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Linea_Abierta_Ratings')


# ### Living Dialogues

# In[62]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Living_Dialogues_Ratings')


# ### Local PM Headlines Spanish

# In[63]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Local_PM_Headlines_Spanish_Ratings')


# ### Making Contact

# In[64]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Making_Contact_Ratings')


# ### Metro

# In[65]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Metro_Ratings')


# ### Metro Arts

# In[66]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Metro_Arts_Ratings')


# ### Morning Magazine

# In[67]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Morning_Magazine_Ratings')


# ### Naturally

# In[68]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Naturally_Ratings')


# ### New Dimensions

# In[69]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'New_Dimensions_Ratings')


# ### Outsources

# In[70]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Outsources_Ratings')


# ### Pasa La Voz

# In[71]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Pasa_La_Voz_Ratings')


# ### Peace Talks

# In[72]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Peace_Talks_Ratings')


# ### Project Censored

# In[73]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Project_Censored_Ratings')


# ### Rising Up with Sonali

# In[74]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Rising_Up_with_Sonali_Ratings')


# ### Sprouts

# In[75]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Sprouts_Ratings')


# ### StoryTellers of Color

# In[76]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'StoryTellers_of_Color_Ratings')


# ### Laura Flanders

# In[77]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Laura_Flanders_Ratings')


# ### Ralph Nader

# In[78]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Ralph_Nader_Ratings')


# ### Shortwave Report

# In[79]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Shortwave_Report_Ratings')


# ### The World

# In[80]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'The_World_Ratings')


# ### TRENDS

# In[81]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'TRENDS_Ratings')


# ### Tributaries

# In[82]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Tributaries_Ratings')


# ### TUC Radio

# In[83]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'TUC_Radio_Ratings')


# ### WINGS

# In[84]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'WINGS_Ratings')


# ### Weed Between

# In[85]:


create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, 'Weed_between_Ratings')

