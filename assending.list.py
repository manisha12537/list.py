my_list = [15, 26, 15, 1, 23, 64, 23, 76]
i=0
list=[]
while i<len(my_list):
    j=my_list[0]
    for k in my_list:
        if j>k:
            j=k
    list.append(j)
    my_list.remove(j)
i=i+1
print(list)
    






       
        

