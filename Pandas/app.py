import pandas as pd

#read data from CSV file into a dataframe
df = pd.read_csv("sample_employees.csv",encoding="latin1")

# df = pd.read_excel("sample_employees.xlsx",encoding="latin1")

# df = pd.read_json("sample_employees.json")
print(df)