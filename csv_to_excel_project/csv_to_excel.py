import pandas as pd
#Reading CSV File
df=pd.read_csv("data.csv")
#Handeling Missing Value
df=df.fillna("Not Available")
#Save data to Excel
df.to_excel("output.xlsx",index=False)
#print Sucess Message
print("CSV to Excel Conversion Completed")
