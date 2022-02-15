list=[7,6,5,4,3,5,6,7,9,2]
list2=[]
for i in list:
    if list.count(i)>1:
        list2.append(list[i])
print(list2)
