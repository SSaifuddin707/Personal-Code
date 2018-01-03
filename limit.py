#edit this function to the equation you want to calculate

def g():
    x = input("what is your x?")
    limit = (((float(x)**2 - 3 * float(x))) / ((float(x)**2 - 9)))
    print("Limit=", limit)
    g()
    

g()
