char_list=["a","n","t","y","a","t","y","m","n","n","a","a","n","n","n"]
i=0
a=[]
while i<len(char_list):
    j=0
    k=[]
    count=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count=count+1
        j=j+1
    k.append(char_list[i])
    k.append(count)
    b=0
    while b<len(k):
        if k not in a:
            a.append(k)
        b=b+1
    i=i+1
print(a)





























# i=0
# a=[]
# while i<len(char_list):
#     j=0
#     b=[]
#     count=0
#     while j<len(char_list):
#         if char_list[i]==char_list[j]:
#             count=count+1
#         j=j+1
#     b.append(char_list[i])
#     b.append(count)
#     if b not in a:
#         a.append(b)
#     i=i+1
# print(a)

            




# char_list=["a","n","t","y","a","t","y","m","n","n","a","a","n","n","n","b,","i"]
# i=0
# d=[]
# while i<len(char_list):
#         if char_list[i]=="a" or char_list[i]=="e" or char_list[i]=="i" or char_list[i]=="o" or char_list[i]=="u":
#             if char_list[i] not in d:
#                 d.append(char_list[i])
#         i=i+1
# print(d)
