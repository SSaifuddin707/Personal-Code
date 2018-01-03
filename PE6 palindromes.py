string= input("Input a alphabetic string\n")
L = len(string)

begin= str(string[0:L])
backward= string[::-1]
print(backward)


if (begin == backward):
    print("Your String is a palindrome!")
    
else:
    print("Your String is not a palindrome")
            

place= input("End")

