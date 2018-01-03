#password generator
import random
import string

password = string.ascii_letters + string.digits + "!@#$%^&*?/=+_-"


def PG(request):
    
    if request == "1":
        size = random.randint(3,6)
        reqpass = "".join(random.sample(password, size))

    if request == "2":

        size = random.randint(6,9)
        reqpass = "".join(random.sample(password, size))

    if request == "3":

        size = random.randint(9,13)
        reqpass = "".join(random.sample(password, size))
    print("\n\t\t\t Your Password is:" + reqpass)

statement = False
while not statement:
    request= (input("Please choose which type of password you would like from the following:\n1. Weak [3 to 5 characters]\n2. Medium [5 to 8 characters]\n3. Strong [8 to 12 characters]\n"))
    
    if (request == "1") ^ (request == "2") ^ (request == "3"):
        statement = True
        break
    else:
        print("You have selected the wrong input, please select from the below listed!")
PG(request)

