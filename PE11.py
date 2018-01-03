#Gets random list and prints list endings
import random
x = random.sample(range (10), 5)
def listES():
    listS = x[0]
    listE = x[-1]
    y = [listS, listE]
    print("List=", x)
    print("list Endings=", y)
listES()

place= input("end")