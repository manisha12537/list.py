list=[7,6,5,4,3,5,6,7,9,2]
j=[]
for i in list:
    if list.count(i)>1:
        if list[i] not in j:
            j.append(list[i])
        i=i+1
print(j)