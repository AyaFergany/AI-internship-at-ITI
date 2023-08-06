import pandas  as pd
import numpy as np
s=pd.Series([2,3,4])
print(s.describe())
print("----------------------------------------")

#s=pd.Series(["p","p","q","r"])
#print(s.describe())
#print("-----------------------------------------")

#df=pd.DataFrame({"categorical":pd.Categorical(["s","t","u"]),"numeric":[2,3,4],"object":["p","q","r"]})
#print(df)
#print(df.describe())
#print(df.describe(include="all"))
#print(df.describe(include=["category"]))
##print(df.describe(exclude=[np.object]))
#print("--------------------------------------------")

#salaries=pd.read_csv("salaries.csv")
#print(salaries.head())
##print(salaries.describe())
#print("-------------------------------------------------")

# read file content as string
##f=open("file.txt","r")
#lines=f.readlines()
#for line in lines:
#    print(line)
    
#with open("file.txt","r") as file:
#    fileContent=file.read()
##    print(fileContent)
#print(file.closed)
#print(fileContent) 

#with open("file.txt","a") as file:
#    file.write("Hi there!")
    
#print("--------------------------------------------------")
# write cvs       
#import csv
#with open("people.csv","w", newline="") as file:
#     write=csv.writer(file)
     
#     writer =csv.writer(file, delimiter="\t")
#     writer.writerow(["SN","Movie","Protagonise"])
 #    writer.writerow([1,"Lord of the Rings","Frodo Baggins"])
 #    writer.writerow([2 ,"Harry Potter","Harry Potter"])
# read file in CVS
#with open("people.csv","r") as file:
#    reader=csv.reader(file)
#    for row in reader:
 #       print(row)