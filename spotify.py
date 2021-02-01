# data manuipulation
import numpy as np
import pandas as pd
import pandas_profiling

# plotting libraries
import matplotlib.pyplot as plt
from ipywidgets import interact
import seaborn as sns
%matplotlib inline

plt.style.use("fivethirtyeight")
sns.set_style('whitegrid')
sns.set_context('talk')

spotify_df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-21/spotify_songs.csv')
spotify_df.head()

spotify_df.dropna(axis=0)
spotify_df = spotify_df.drop(["track_id","track_album_id", "playlist_id"], axis= 1)

spotify_df.rename(columns={'track_name':"title",'track_artist':'artist','track_popularity':'title_popularity',
                        'track_album_name':'album','track_album_release_date':'album_release_date'},inplace=True)

print("The spotify_df_df_df dataset entails " + str(spotify_df.artist.nunique()) + " unique artists")

spotify_df['album_release_date'] = pd.to_datetime(spotify_df.album_release_date)

# create year column
spotify_df['album_release_year'] = pd.DatetimeIndex(spotify_df['album_release_date']).year

# create month column
spotify_df['album_release_month'] = pd.DatetimeIndex(spotify_df['album_release_date']).month

# create day column
spotify_df['album_release_day'] = pd.DatetimeIndex(spotify_df['album_release_date']).day

popularity_df = spotify_df.groupby("title")["title_popularity"].mean().sort_values(ascending=False).head(10)
popularity_df = pd.DataFrame(popularity_df).reset_index()
popularity_df

spotify_df_sorted = spotify_df.sort_values("title_popularity", ascending = False).drop_duplicates(subset=["title","artist"])
spotify_df_sorted.head(5)

def cat(var):
    ax = sns.catplot(y = "playlist_genre", 
                kind = "count", 
                data = spotify_df_sorted.iloc[:var,],)
    plt.title('Count of Top Songs by Genre')
    plt.show()

int_catplot = interact(cat, var = (10,10000,100),)
int_catplot