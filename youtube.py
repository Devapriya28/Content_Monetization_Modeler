#import pandas as pd

#utube=pd.read_csv(r"D:\DATA SCIENCE\DATASET\youtube_ad_revenue.csv")

#utube

#UNDERSTAND THE DATA

#utube.info()

#utube.describe()

#utube.nunique()

#utube.duplicated().sum()

#utube.isnull().sum()

#utube.columns

#VISHUALIZING THE DATA

#numerical_columns=['views', 'likes', 'comments', 'watch_time_minutes',
#       'video_length_minutes', 'subscribers', 'ad_revenue_usd']

#print(utube[numerical_columns].describe())
#import matplotlib.pyplot as plt
#import seaborn as sns
#import plotly.express as px

'''for col in numerical_columns:
    fig = px.histogram(
        utube, 
        x=col, 
        nbins=50, 
        marginal="box",   # box plot above histogram
        title=f"Distribution of {col}", 
        opacity=0.75
    )
    fig.show()

for col in numerical_columns[:-1]:  # exclude target
    fig = px.scatter(
        utube,
        x=col,
        y='ad_revenue_usd',
        size='views',         # bubble size based on views
        color='category',     # optional: color by category
        hover_data=['likes', 'comments'],  # extra info on hover
        title=f"{col} vs Ad Revenue Bubble Chart",
        size_max=40
    )
    fig.show()
import plotly.express as px

for col in numerical_columns:
    fig = px.box(
        utube,
        x=col,
        points="all",          # show all data points, outliers included
        title=f"Outlier Detection - {col}"
    )
    fig.show()'''

