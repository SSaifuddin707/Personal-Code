import random

listA= random.sample(range(50), 10)
listB= random.sample(range(50), 13)


print("List A :", listA)
print("List B :", listB)


listC =[element for element in listA for elements in listB if element ==elements]

#for element in listA:
#    for elements in listB:
#        if (element==elements):
#            listC.append(element)
        
    
print("Similarities:", listC)

#updated as of 10/19/2017)
