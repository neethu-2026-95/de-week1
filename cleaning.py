import pandas as pd
df=pd.read_csv("titanic.csv")
print("original shape:",df.shape)
print("\n Missig values per column:")
print(df.isnull().sum())
# Fill missing Age with the median age
median_age=df["Age"].median()
df["Age"]=df["Age"].fillna(median_age)
print("Median age used:",median_age)
print("Missing Age after fix:",df["Age"].isnull().sum())
# Fill missing Embarked with most common port
most_common_port = df["Embarked"].mode()[0]
df["Embarked"] = df["Embarked"].fillna(most_common_port)

print("Port used:", most_common_port)
print("Missing Embarked after fix:", df["Embarked"].isnull().sum())

# Drop Cabin — too many missing values to be useful
df = df.drop(columns=["Cabin"])

print("Columns after dropping Cabin:", df.columns.tolist())
print("Final missing values:")
print(df.isnull().sum())
# All zeros — clean dataset!

# Save cleaned data — never overwrite raw data!
df.to_csv("titanic_clean.csv", index=False)
print("\nClean data saved as titanic_clean.csv")
print("Final shape:", df.shape)