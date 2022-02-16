element=[4,5,6,78,99,24,44,55,73,49,11]
even_list=[]
odd_list=[]
for i in element:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print("even_list: ",even_list)
print("odd_list: ",odd_list)




# i=0
# odd=[]
# even=[]
# while i<len(element):
#     if element[i]%2==0:
#         odd.append(element[i])
#     else:
#         even.append(element[i])
#     i=i+1
# print(odd)
# print(even)