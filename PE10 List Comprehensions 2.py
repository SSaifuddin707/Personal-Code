listA = [1, 1, 2, 3, 5, 5, 8, 13, 21, 34, 55, 89]
listB = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
listC =[set(element for element in listA for elements in listB if element == elements)]


print(listA)
print(listB)
print("Similiarities:", listC)
