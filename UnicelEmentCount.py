input_list = [1, 2, 2, 5, 8, 4, 4, 8]
j=[]
count=0
for i in input_list:
    if i not in j:
        j.append(i)
for k in j:
    count=count+1
print(count)







