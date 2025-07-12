"""
1-how big is your dataset
2- what are names  of column

shape and column
"""

import pandas as pd

data={

    "Name":["Ram","Shyam","Hari","Gita","Ravi","Laxmi"],
    "Age":[20,21,22,23,24,25],
    "Salary":[75000,68000,62000,77000,55000,60000],
    "Performance Score":[85,90,78,92,95,80]


}

DF = pd.DataFrame(data)
print("Shape of the Dataset",DF.shape)
print("Column Names",DF.columns)