import math
x = input("what is your x?")

def g():
    if x == float():
        limit = ((math.log(float(x))) - (math.log(4))) / ((float(x)-4))
        print("Limit=", limit)
        g()
    
    else:
        print("Thank you for using this function!")
        return

g()
#not working lol
