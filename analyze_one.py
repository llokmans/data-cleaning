import pandas as pd

employees = pd.read_csv("cleaned_data.csv")
departments = pd.read_csv("departments.csv")

inner = pd.merge(employees, departments, on="department", how="inner")
print("----- INNER JOIN -----")
print(inner[["first_name", "department", "manager", "floor"]])

left = pd.merge(employees, departments, on="department", how="left")
print("----- LEFT JOIN -----")
print(left[["first_name", "department", "manager", "floor"]])


missing_dept = left[left["manager"].isnull()]
print(missing_dept[["first_name", "department"]])