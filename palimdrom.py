# # num=input("enter name")
# # i=0
# # j=-1
# # while i<len(num):
# #     if num[i]==num[j]:
# #         print("pailndrom")
# #         break
# #     else:
# #         print("not pailndrom")
# #         break            


# list=input("enter ame")
# i=0
# a=[]
# b=[]
# while i<len(list):
#     count=0
#     m=list[i]
#     j=0
#     while j<len(list):
#         n=list[j]
#         if n==m:
#             count=count+1
#             b.append(n)
#         j=j+1
#     k=0
#     while k<len(list):
#         if m not in a:
#             a.append(m)
#             print(m,count)
#         k=k+1
#     i=i+1
# # print(a)


# def m(f):
#     print(f)
# a=['a', 1, '2', 5, 'b', 'q']
# m(a)



# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3={}
# for i,j in d1.items():
#   for k,l in d2.items():
#     if k==i:
#       d3[i]=(j+l)
# for m in (d2,d3):
#   d1.update(m)
# print(d1)


Data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
for i in Data:
  for j in i.keys():
    print(j)






# list=input("enter charactor")
# i=0
# k=-1
# while i<len(list):
#     if list[i]==list[k]:
#         pailndrom=True
#     else:
#         pailndrom=False
#     k=k-1

#     i=i+1
# print(pailndrom)