import pandas as pd

df = pd.read_csv('Pandas/imdb.csv')

result = df.tail(10)

result=df["original_title"]

result=df["original_title"].head()

result=df[["original_title", "vote_average"]].head(7)
result=df[["original_title", "vote_average"]]

result=df[df["vote_average"]>=8][["original_title", "vote_average"]].head(50)

df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
result = df[(df['release_date'].dt.year >= 2014) & (df['release_date'].dt.year <= 2015)][['title']]


result = df[(df["revenue"] > 13000000.0) | (df["vote_average"] > 7)]



print(result)
