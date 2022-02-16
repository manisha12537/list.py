list=[45,6,6,7,7,8,9,0,1,2,3,2,3]
duplicate_list=[]
for i in list:
    if list.count(i)>1:
        if i not in duplicate_list:
            duplicate_list.append(i)
print(duplicate_list)
