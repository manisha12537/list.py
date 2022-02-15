list=["m","o","m"]
i=0
j=-1
while i<len(list):
    if list[i]==list[j]:
        pailndrom=True
    else:
        pailndrom=False
    j=j-1
    i=i+1
print(pailndrom)