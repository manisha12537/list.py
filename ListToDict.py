list=[["a",5],["b",3],["c",9],["d",6]]
i=0
dict={}
while i<len(list):
    j=0
    while j<len(list[i]):
        k=1
        while k<len(list[i]):
            dict.update({list[i][j]:list[i][k]})
            k=k+2
        j=j+2
    i=i+1
print(dict)
