import pandas as pd

data={
    "Name":["Shivam","Niraj","Anurag","Nitesh"],
    "Age":[12,19,34,20],
    "Salary":[34000,45000,33200,56000]
}
df=pd.DataFrame(data)

#adding column in the data 
#df["column_name"]=some_Data
print(df)


df["Bonus"] = df["Salary"] * 0.1 
print(df)


#Using insert method 
# df.insert[location of column,"name of column",data]

df.insert(2,"New Location",df["Name"]+"Shivam")
print(df)






## Updating Values in the data


#.loc[]
#df.loc[row_index,"Column Name"]=new value

df.loc[0,"Salary"]=45000  #Changing the value of Salary column and the 0th row with value 45000
print(df)

df["Salary"] = df["Salary"] + df["Bonus"]
print(df)



## Removing Column

df.drop(columns=["Age"],inplace=True)  #inplace=True indicates that it is replacing the original one
print(df)


