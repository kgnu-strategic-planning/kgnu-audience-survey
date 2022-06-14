import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import MaxNLocator
from IPython.display import display, Markdown


def create_hist_and_stats(df, filter_col, filter_col_val, filter_col_val_display, col):
    if filter_col == 'all_respondents':
        df_filtered = df
    elif filter_col == 'other_counties':
        df_filtered = df[~df['County'].isin(['Boulder', 'Denver', 'Jefferson', 'Arapahoe', 'Adams', 'Larimer', 'Weld', 'Douglas', 'Broomfield'])]
    else:
        df_filtered = df[df[filter_col] == filter_col_val]

    if df_filtered[col].dropna().count() == 0:
        print(filter_col_val_display)
        print('Total Respondents: 0')
        return        
        
    df_filtered[col].value_counts().plot.bar(rot=90)
    plt.title(col)

    axes = plt.gca()       
    ya = axes.get_yaxis()
    ya.set_major_locator(MaxNLocator(integer=True))

    plt.xlabel('Rating')
    plt.ylabel('Number of Respondents')

    plt.show()
    
    print(filter_col_val_display)

    ra = df_filtered[col].apply(pd.to_numeric, errors='coerce')
    print(f'Total Respondents: {df_filtered[col].dropna().count()}')
    print(f'Respondents Familiar with Show: {ra.dropna().count()}')

    percent_familiar = (ra.dropna().count()/df_filtered[col].dropna().count()) * 100   
    print(f'Percent Familiar with Show: {percent_familiar:.1f}%')

    if ra.dropna().count() > 0:
        print(f'Median: {int(ra.dropna().median())}')
        print(f'Mean: {ra.dropna().mean():.2f}')
        
        
def create_regular_outlet_users_by_importance_preference(df, importance_col, importance_name):
    media_outlets = ['Denver Post', 'Westword', 'PBS-12', 'KUNC-91.5', 'The Longmont Leader', 'Indie-102.3', 'KFRC-88.9-FM', \
                     'Boulder Reporting Lab', 'Boulder Beat', 'KGNU', 'Denverite', 'CPR', '105.5-The Colorado Sound', 'Boulder Weekly', \
                     'Rocky Mountain PBS', 'KUVO-89.3-FM', 'Colorado Sun', 'Daily Camera', 'Ideal Station']
    
    df_filtered_1 = df[(df[importance_col]=='10 - Very Important') | (df[importance_col]==9)]

    num_users = []
    colors = []

    for media_outlet in media_outlets:
        col = media_outlet.replace(' ', '_') + '_Frequency_Used'
        if col == 'Ideal_Station_Frequency_Used':
             df_filtered = df[((df[importance_col]=='10 - Very Important') | (df[importance_col]==9))  & (df[col]=='Regularly - 4 or more days a week') ]
        else:
            df_filtered = df[((df[importance_col]=='10 - Very Important') | (df[importance_col]==9))  & (df[col]=='Familiar - Use Regularly') ]
        #print(f'{col}:  {len(df_filtered)}')

        num_users.append(len(df_filtered))


    zipped_lists = zip(num_users, media_outlets)
    sorted_pairs = sorted(zipped_lists, reverse=True)
    tuples = zip(*sorted_pairs)
    num_users, media_outlets = [ list(tuple) for tuple in  tuples]

    for outlet in media_outlets:
        if outlet == 'KGNU':
            colors.append('red')
        else:
            colors.append('grey')
            
    plt.bar(media_outlets, num_users, color = colors, width = 0.5)
    plt.xticks(rotation = 90)
    plt.xlabel('Media Outlets')
    plt.ylabel('Number of Regular Users')
    plt.title(f'Regular Users of Media Outlets\nFrom the pool of those who value "{importance_name}"')
    plt.show()

    print(f'Cohort is defined those who rated "{importance_name}" at least a 9 in Importance.')
    print(f'Cohort Size: {len(df_filtered_1)}')
    print()
    
    print('Within this Cohort, % "Regular User" Statistics:')
    print()
    for i, val in enumerate(media_outlets):
        percent = (num_users[i]/len(df_filtered_1)) * 100   
        print(f'{val}: {percent:.1f}%')


