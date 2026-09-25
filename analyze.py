import pandas as pd

df = pd.read_csv("cleaned_data.csv")
print(df)

departments = df['department'].unique()

for department in departments:
    department_filter = df[df['department'] == department]

print(df.groupby("department")["salary"].mean())

print(df.groupby("department")["salary"].agg(["mean", "sum", "count"]))


print(df.groupby("status")["id"].count())