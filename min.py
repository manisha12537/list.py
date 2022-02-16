
dict={"a":5,"b":8,"c":9,"d":4}
for i,j in dict.items():
    for k,l in dict.items():
        if j>l:
            j=l
print(j)
    

