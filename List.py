# list=["manisha","suresh","mavaskar"]
# i=0
# list2=[]
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         k=list[i][j]
#         list2.append(k)
#         j=j+1
#     i=i+1
# print(list2)


a=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c','a']
k=len(a)-1-a[::-1].index("k")
print(k)

        