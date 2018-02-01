import pandas as pd

df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)

print(df.columns)

df.columns = ["month", "passengers"]

print(df.columns)

print(df['passengers'])
# String and no space, can do this
print(df.passengers)

# Add a column with all same values
df['ones'] = 1
print(df.head())
