element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
c=0
d=0
while i<len(element):
    if element[i]%2==0:
        c=c+1
    else:
        d=d+1
    i=i+1
print("even_count: ",c)
print("odd_count: ",d)




# c=0
# d=0
# for i in element:
#     if i%2==0:
#         c=c+1
#     else:
#         d=d+1
# print("even_count: ",c)
# print("odd_count: ",d)



