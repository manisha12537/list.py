list=[45,787,00,765,22,45,87,98,31,454]
i=0
list1=[]
while i<len(list):
    if list[i]>20 and list[i]<40:
        list1.append(list[i])
    i=i+1
print(list1)