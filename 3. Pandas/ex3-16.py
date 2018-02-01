import pandas as pd
from datetime import datetime

df = pd.read_csv("international-airline-passengers.csv", engine="python", skipfooter=3)

print(datetime.strptime("1949-05", "%Y-%m"))

df.columns = ["month", "passengers"]
df['ones'] = 1

df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)

print(df.info())
