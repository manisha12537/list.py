list=[2,10,2,22,37,44,2,51,98,2,4]
i=0
list2=[]
while i<len(list):
    j=0
    list3=[]
    while j<2:
        list3.append(list[i])
        j=j+1
    if list3 not in  list2:
        list2.append(list3)
    i=i+1
print(list2)