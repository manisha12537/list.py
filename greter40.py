list=[[23,76,45,9],[34,87,31],[23,44],[67,98,23,5]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]>40:
            print(list[i][j])
        j=j+1
    i=i+1