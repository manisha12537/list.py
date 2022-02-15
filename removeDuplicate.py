list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
i=0
j=[]
while i<len(list):
    if list[i] not in j:
        j.append(list[i])
    i=i+1
print(j)

