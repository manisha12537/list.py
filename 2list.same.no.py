list1=[45,65,79,77,80,21]
list2=[45,68,89,21,43,65]
list3=[]
for i in list1:
    if i  in list2:
        list3.append(i)
print(list3)