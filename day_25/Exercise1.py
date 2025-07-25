#Exercise 1
import pandas as pd
import numpy as np
#1
df = pd.read_csv('hacker_news.csv')

#2
print(df.head())

#3
print(df.tail())

#4
def title(dataframe):
    title_series = dataframe['title']
    return title_series

print(title(df))

#5
def count_rows_columns(dataframe):
    rows, columns = dataframe.shape
    return f'There are {rows} rows and {columns} columns in the dataframe.'

print(count_rows_columns(df))

def title_only_py(dataframe):
    python_titles = dataframe[dataframe['title'].str.contains('python', case=False, na=False)]
    return python_titles['title']

print(title_only_py(df))

def title_only_js(dataframe):
    javascript = dataframe[dataframe['title'].str.contains('javascript', case=False, na=False)]
    return javascript['title']

print(title_only_js(df))

