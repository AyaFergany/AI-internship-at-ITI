import csv
import pandas  as pd
import numpy as np
n=1
l=[]

with open('people.csv','w', newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age','salary'])
    for i in range (10):
        lst=[]
        name=input("Enter name of people :")
        lst.append(name)
        age=input("Enter age of people:")
        lst.append(age)
        salary=input("Enter salary of people :")
        lst.append(salary)
        n+=1
        l.append(lst)

        writer.writerow(lst)

# read file in CVS
with open("people.csv","r") as file:
    people=pd.read_csv('people.csv')
    print(people.head(3))
    print(people.tail(3))
    value_age=pd.read_csv('people.csv',usecols=['age'])
    print(value_age.describe())
   