import pandas as pd

data={
    "Name":["Shivam","Niraj","Anurag","Nitesh"],
    "Age":[12,19,34,None],
    "Salary":[34000,45000,33200,None]
}
df=pd.DataFrame(data)
print(df.isnull())
print(df.isnull().sum())

#Dropping missing Data
df.dropna(axis=1,inplace=True)
print(df)

#fillna method to fill missing value with average or anything  you want

df.fillna(500,inplace=True)
print(df)


##Interpolation  (Filling missing value with some estimated value for numerical column based on mathematics)
# Works with time series data like stock market
# Avoid deleting rows directly
# interpolation avoid data loss , preserve integrity and smooth trends


df["Salary"] = df.interpolate(method="linear",axis = 0 , inplace =True)
print(df)