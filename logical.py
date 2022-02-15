k=[1234, 122, 1984, 19372, 100]
i=0
list=[]
while i<len(k):
    j=0
    p=str(k[i])
    a=p[0]
    list.append(a)
    print(list)
    f=0
    while f<len(list):
        m=list[0]
        f=f+1
    p=0
    while p<len(list):
        if m==list[p]:
            same=True
        else:
            same=False
        p=p+1

    i=i+1
print(same)