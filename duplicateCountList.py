list=["a","s","e","a","r","g","r","a","b","t"]
i=0
list2=[]
while i<len(list):
    count=0
    k=0
    list1=[]
    while k<len(list):
        if list[i]==list[k]:
            count=count+1
        k=k+1
    list1.append(list[i])
    list1.append(count)
    if list1 not in list2:
        list2.append(list1)
    i=i+1
print(list2)
    
