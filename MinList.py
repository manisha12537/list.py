list=[67,89,23,45,65,12,34]
i=0
j=list[0]
while i<len(list):
    if j>list[i]:
        j=list[i]
    i=i+1
print(j)
