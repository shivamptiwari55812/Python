import pandas as pd

data={
    "Name":["Shivam","Niraj","Anurag","Nitesh"],
    "Age":[12,19,34,20],
    "Salary":[34000,45000,33200,56000]
}
df=pd.DataFrame(data)

#Sorting data alphabetically, Ascending = True 
# df.sort_values(by="Name", ascending = True , inplace=True)
# print("Sorted age by descending")
print("Before sorting",df)

df.sort_values(by=["Name","Age"],ascending = [True,True] , inplace=True)
print("After sorting")
print(df)


##Aggregation 

# df["Any column"].mean()/.sum()/.max()