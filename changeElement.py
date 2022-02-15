list=[2,10,2,22,37,44,2,51,98,2,4]
i=0
while i<len(list):
    if list[i]==2:
        list[i]=0
    i=i+1
print(list)