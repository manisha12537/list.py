list=[[23,76,45,9],[34,87,31],[23,44],[67,98,23,5]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        k=list[i][j]
        a=0
        while a<len(list[i]):
            if k>list[i][a]:
                k=list[i][a]
            a=a+1
        j=j+1
    i=i+1
print(k)