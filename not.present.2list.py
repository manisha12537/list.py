list=[1,2,3,4,5,6]
list1=[2,3,1,0,6,7]
a=[]
for i in list:
    if i not in list1:
        a.append(i)
print(a)