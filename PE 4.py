#code returns the divisors for the input number
num = int(input("Type a number for its divisers"))

listRange = list(range(1, num + 1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

divisorList2 = [number for number in listRange if (num % number) == 0]
        
print(divisorList)
print(divisorList2)

#updated as of 10/19/2017)
