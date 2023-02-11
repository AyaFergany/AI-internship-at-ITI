lst1 = [10, 20, 30, 40, 50]
lst2 = [5, 10, 15, 20, 25, 30, 35, 40]
lst3 =[]
for i in lst1:
    for j in lst2:
        if i == j:
            lst3.append(i)
print(lst3)
