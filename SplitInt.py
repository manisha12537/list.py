list= [123, 67, 98, 34]
i=0
sum=0
while i<len(list):
    j=0
    k=str(list[i])
    while j<len(k):
        p=int(k[j])
        sum=sum+p
        j=j+1
    i=i+1
print(sum)



