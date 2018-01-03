def g():
    x = input("what is your x?")
    limit = ((((float(x) + 2)**5) - 32)/ (float(x)))
    print("Limit=", limit)
    g()
    

g()
