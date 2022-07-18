import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pylab import MaxNLocator
from IPython.display import display, Markdown

rankings = {}


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
        
        num, music_num, news_num, is_music_show = rankings[col]
        print(f'Overall Ranking: {num}')
        if is_music_show:       
            print(f'Music-Show Ranking: {music_num}')
        else:
            print(f'News-Show Ranking: {news_num}')
        
        
def create_ranked_table_of_shows(df, random, filter_col, filter_col_val, filter_col_val_display):
    if random:
        show_ratings_cols = df.columns.tolist()[97:177]
        music_show_ratings_cols = df.columns.tolist()[97:132]
    else:
        show_ratings_cols = df.columns.tolist()[111:191]
        music_show_ratings_cols = df.columns.tolist()[111:146]
        
    if filter_col == 'all_respondents':
        df_filtered = df
    elif filter_col == 'other_counties':
        df_filtered = df[~df['County'].isin(['Boulder', 'Denver', 'Jefferson', 'Arapahoe', 'Adams', 'Larimer', 'Weld', 'Douglas', 'Broomfield'])]
    else:
        df_filtered = df[df[filter_col] == filter_col_val]
        

    list_of_dicts = [] 
    for col in show_ratings_cols:
        ra = df_filtered[col].apply(pd.to_numeric, errors='coerce')
        total_respondents = df_filtered[col].dropna().count()
        num_familiar_with_the_show = ra.dropna().count()
        percent_familiar = (ra.dropna().count()/df_filtered[col].dropna().count()) * 100   
        ranking_score = int(ra.dropna().sum())
        
        median = 0
        mean = 0
        if ra.dropna().count() > 0:
            median = int(ra.dropna().median())
            mean = ra.dropna().mean()
             
        show_name = col.replace('_Ratings', '')
        show_name = show_name.replace('_', ' ')
        
        #ranking_score = num_familiar_with_the_show * mean
        
        dict = {'Col_Name':col, 
                'Show':show_name, 
                'Num_Respondents':total_respondents, 
                'Num_Familiar':num_familiar_with_the_show, 
                'Percent_Familiar':percent_familiar, 
                'Median':median, 'Mean':mean, 
                'Ranking_Score':ranking_score}
        
        list_of_dicts.append(dict)
        
    da = pd.DataFrame(list_of_dicts)
    da.sort_values(by=['Ranking_Score'], ascending=False, inplace=True)
    
    print(f'Overall      Show               #Ratings/    Median/Mean  Score   Music   News')
    print(f'Ranking                        #Respondents                       Show    Show')
    print(f'                                                                 Ranking Ranking')
    print(f'--------------------------------------------------------------------------------')
    
    num = 0
    music_num = 0
    news_num = 0
    last_score = 10000
    last_music_score = 100000
    last_news_score = 100000
    for index, row in da.iterrows():
        if row["Ranking_Score"] < last_score:
            last_score = row["Ranking_Score"]
            num += 1
            
        ratings_resp = str(row["Num_Familiar"]) + '/' + str(row["Num_Respondents"])
        
        if row['Col_Name'] in music_show_ratings_cols:
            if row["Ranking_Score"] < last_music_score:
                last_music_score = row["Ranking_Score"]
                music_num += 1            
            print(f'{num:>2}    {row["Show"]:<28}{ratings_resp:>7}       {row["Median"]:>2}/{row["Mean"]:.1f}    {row["Ranking_Score"]:>4}     {music_num:>2}') 
            rankings[row['Col_Name']] = (num, music_num, news_num, True)

        else:
            if row["Ranking_Score"] < last_news_score:
                last_news_score = row["Ranking_Score"]
                news_num += 1  
            print(f'{num:>2}    {row["Show"]:<28}{ratings_resp:>7}       {row["Median"]:>2}/{row["Mean"]:.1f}    {row["Ranking_Score"]:>4}             {news_num:>2}') 
            rankings[row['Col_Name']] = (num, music_num, news_num, False)
        
        

