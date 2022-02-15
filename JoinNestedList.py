a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
while i<len(a):
    k=a[i]
    if type(k) is list:
        p=0
        while p<len(k):
            b[i].append(k[p])
            p=p+1
    i=i+1
print(b)    