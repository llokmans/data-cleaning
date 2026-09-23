import pandas as pd

df = pd.read_csv("messy_data.csv")
print(df)


print("-----DUPLICATED USERS----")
print(df[df.duplicated()])

df = df.drop_duplicates()
print(df)
print(f"Duplicates remaining: {df.duplicated().sum()}")


df["status"] = df["status"].str.lower()
df["email"] = df["email"].str.lower()
print(df)
print(f"Fixed successfully")

df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
print(df)
print(f"Returned Salary")

df["hire_date"] = pd.to_datetime(df["hire_date"], errors="coerce", format="mixed")
print(df)
print(f"Fixed Dates")

median_salary = df["salary"].median()
df["salary"] = df["salary"].fillna(median_salary)
print(df)

df["last_name"] = df["last_name"].fillna("Unknown")
print(df)

df.to_csv("cleaned_data.csv", index=False)