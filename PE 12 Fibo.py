#function for fibonacci sequence
def fibo():
    amount = int(input("How many numbers would you like to display in the Fibonacci Sequence?\n"))
 

    o = 1
    if amount == 0:
        fib = []
    elif amount == 1:
        return 1
    elif amount == 2:
        fib = [1,1]
    elif (amount > 2) and (amount < 10001):
        fib = [1,1]
        while o <(amount - 1): 
            fib.append(fib[o] + fib[o-1])
            o += 1
        print(fib)
    else:
         print("Whoa there cowboy! This is only IDLE!!!!")
    
fibo()

placeholder = input("")
        
