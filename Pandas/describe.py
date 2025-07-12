import pandas as pd

data={

    "Name":["Ram","Shyam","Hari","Gita","Ravi","Laxmi"],
    "Age":[20,21,22,23,24,25],
    "Salary":[75000,68000,62000,77000,55000,60000],
    "Performance Score":[85,90,78,92,95,80]

}

df =pd.DataFrame(data)
print(df)
print("Descriptive Statistics")
print(df.describe())

## small standard deviation means values are nearly close . And the s.d is large when data is inconsistent
