binary_number=[1,0,0,1,1,0,1,1]
paise=[300,60000,65657676,877877789,432322432434,90000,876765,4535342,121213123,32344]
i=0
lakhpati=[]
karodpati=[]
dilwale=[]
while i<len(paise):
    if paise[i]>=100000 and paise[i]<10000000:
        lakhpati.append(paise[i])
    elif paise[i]>=10000000:
        karodpati.append(paise[i])
    elif paise[i]<100000:
        dilwale.append(paise[i])
    i=i+1 
print("lakhpati",lakhpati)
print("karodpati",karodpati)
print("dilwale",dilwale)


