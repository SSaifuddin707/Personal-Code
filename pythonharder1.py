numList = []

for x in range(2000, 3200):
    if (int(x)%7 == 0) and not (x % 5 == 0):
        numList.append(x)
        
    
print("All numbers divisible by 7 and not 5 between 2000 and 3200:\n", numList)
placeholder = input("")

#solution:

#l=[]
#   if (i%7==0) and (i%5!=0):
#        l.append(str(i))

#print (",".join(l))
