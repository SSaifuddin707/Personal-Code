import random

ans = random.randint(1,100)

counter = 0   


def GG():
    global counter

    guess = int(input("Guess a number between 1 and 100, including 1 and 100!"))
     
    if (guess < 1) or (guess > 100):
        print("Invalid Input. Please guess between 1 and 9!")
        GG()
    elif guess == ans:
        print("Correct! You guessed", ans,"!")
        print("You guessed",counter,"times before winning!")
    elif guess > ans:
        print("Too High!")
        counter += 1
        GG()
    elif guess < ans:
        print("Too Low!")
        counter += 1
        GG()
    elif guess == "exit":
        return
GG()
