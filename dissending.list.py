my_list = [15, 26, 15, 1, 23, 64, 23, 76]
i=0
list=[]

while i<len(my_list):
    j=0
    k=my_list[0]
    while j>len(my_list):
        if k>my_list[j]:
            k=my_list[j]
        j=j+1
    list.append(k)
    my_list.remove(k)
i=i+1
print(list)








   

