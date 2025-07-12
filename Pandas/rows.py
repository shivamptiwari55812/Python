import pandas as pd

#head and Tail methods

df = pd.read_csv("sample_employees.csv")

print("Display initial 3 rows:\n")
print(df.head(3))



#Summary of data

print(df.info())

