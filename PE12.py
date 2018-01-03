
import random

listA= [ 1,1,1,2,2,3,4,4,4,5,5,6,6,7,8,9,9,1]
#random.sample(range(100), 10)
print("List A :", listA)

def noDup(D):
    d = set(D)
    print("No Duplicates:", d)
    return 
noDup(listA)

place= input("end")