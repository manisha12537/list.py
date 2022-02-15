a=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
b=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
i=0
while i<len(b):
    k=b[i]
    if type(k) is list:
        j=0
        while j<len(k):
            a[i].append(k[j])
            j=j+1
        i=i+1
print(a)
