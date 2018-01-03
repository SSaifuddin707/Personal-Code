import math

def g():
    x = input("what is your x?")
    limit = ((math.log(float(x))) - (math.log(4))) / ((float(x)-4))
    print("Limit=", limit)
    if x == float:
        g()
    else:
        print("Thank you for using this function!")
        return

g()
