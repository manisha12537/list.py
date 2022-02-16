# list=[[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
# i=0
# while i<len(list):
#     j=0
#     while j<len(list[i]):
#         if list[i][j]<0:
#             print(list[i][j])
#         j=j+1
#     i=i+1









numbers=[1,3,5,6,[7,8]]

def nested_sum(L):
    sum=0
    for i in range(len(L)):
       if (len(L[i])>1):
          sum=sum+nested_sum(L[i])
       else:
          sum=sum+L[i]
    return sum
nested_sum(numbers)




# def add_all(t):
#     total = 0
#     for i in t:
#         if type(i) == list: # check whether i is list or not
#             total = total + add_all(i)
#         else:
#             total += i
#     return total
# print(add_all(numbers))