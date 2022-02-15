number=5
i=1
list2=[]
while i<=number:
    list=[]
    k=i*i
    list.append(i)
    list.append(k)
    if list not in list2:
        list2.append(list)
    i=i+1
print(list2)
