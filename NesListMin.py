list=[[23,76,45,9],[34,87,31],[23,44],[67,98,23,5]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        k=0
        a=list[i][j]
        while k<len(list[i]):
            if a>list[i][k]:
                a=list[i][k]
            k=k+1
        j=j+1
    i=i+1
print(a)