# 1- select specific column
# 2- filter rows
# 3- combine multiple condition


# filtered_row=df[(df["Salary"]>70000) & (df["Performance Score"]>90)]



import pandas as pd

df=pd.read_csv("sample_employees.csv")
filtered_row=df[(df["Salary"]>70000)]
print(filtered_row)