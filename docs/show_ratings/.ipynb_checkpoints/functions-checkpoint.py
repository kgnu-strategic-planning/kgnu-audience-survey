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

