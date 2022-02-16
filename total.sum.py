number=30
n=[10,12,13,14,17,18,19]
i=0
b=[]
while i<len(n):
    j=len(n)-1
    while j>4:
        if n[i]+n[j]==number:
            b.append([n[i],n[j]])
        j=j-1
    i=i+1
print(b)




# list=['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# list.remove(("p1"))
# print(list)


# list=[9,2,3,4,8,7,6,5]
# i=0
# a=[]
# while i<len(list):
#     j=len(list)-1
#     while j>6:
#         a.append([list[i],list[j]])
#         j=j-1
#     i=i+1
# print(a)



    # if len(list[i])>1:
    #     print(list[i])

    # i=i+1


# num=int(input("enter the number"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#         sum=sum+i
# if sum==num:
#     print("pailndrom")
# else:
#     print("not pailndrom")