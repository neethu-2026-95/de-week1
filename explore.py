import pandas as pd
df = pd.read_csv('titanic.csv')
print(df.head())
print("shape:",df.shape)
print(df.info())
print(df.describe())

survival=df.groupby("Survived")
df["PassengerId"].count()
print (survival)
