import pandas as pd

data =  {
    "Name":["John Doe","Jane Smith","Bob Johnson","Alice Williams","Michael Brown","Linda Davis"],
    "Department":["Engineering","Marketing","Sales","Engineering","HR","Finance"],
    "Position":["Software Engineer","Marketing Manager","Sales Executive","DevOps Engineer","HR Specialist","Accountant"],
    "Email":["john.doe@example.com","jane.smith@example.com","bob.johnson@example.com","alice.williams@example.com","michael.brown@example.com","linda.davis@example.com"],
    "Salary":[75000,68000,62000,77000,55000,60000]
}

df = pd.DataFrame(data)
print(df)

df.to_csv("dataFrame.csv",index=False)
df.to_excel("dataFrame.xlsx",index=False)
df.to_json("DataRequired.json",index=False)