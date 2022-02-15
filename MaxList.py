list=[67,89,23,45,65,12,34]
i=0
k=list[0]
while i<len(list):
    if k<list[i]:
        k=list[i]
    i=i+1
print(k)
    