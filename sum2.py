marks=[[78,76,94,86,88],
    [91,71,98,65],
    [95,45,78]
]
i=0
sum=1
k=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        if marks[i][j]%2==0:
            sum=sum+marks[i][j]
        j=j+1
    i=i+1
print(sum)







































