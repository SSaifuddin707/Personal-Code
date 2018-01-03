import sys
import os
def mainMenu():
    print("\t\t\tMAIN MENU\t\t\t\n")
    print("1. Convert inches to centimeters\n")
    print("2. Convert feet to meters\n")
    print("3. Convert miles to kilometers\n")
    print("4. End Program")
    response = int(input("\nEnter a selection [1-3]\n"))
    if response == 1:
        inTOcent()
    elif response == 2:
        ftTOmet()
    elif response == 3:
        miTOkm()
    elif response == 4:
        sys.exit()
    else:
        print("Invalid input [1-3]. Try Again")
        mainMenu()


def exite(y):
    exite = input("Would you like to try again?[Y/N]\n")
    if exite == "Y" or "y":
        y
    elif exite == "n" or "N":
        mainMenu()

def inTOcent():
    val = int(input("What number would you like to convert (inches to cent)"))
    convert = (val * 2.54)
    print(val, "inches is",convert,"centimeters")
    exite = input("Would you like to try again?[Y/N]\n")
    print(exite, "teset")
    if exite == "Y" or exite == "y":
        inTOcent()
    elif exite == "n" or exite == "N":
        mainMenu()

def ftTOmet():
    val = int(input("What number would you like to convert (feet to meters)"))
    convert = (val * 0.3048)
    print(val, "feet is",convert,"meters")
    exite = input("Would you like to try again?[Y/N]\n")
    if exite == "Y" or "y":
        ftTOmet()
    elif exite == "n" or "N":
        mainMenu()
    

def miTOkm():
    val = int(input("What number would you like to convert (miles to kilometers)"))
    convert = (val * 1.609)
    print(val, "miles is",convert,"kilometers")
    hg = miTOkm()
    exite(hg)
    

mainMenu()   
#response = int(input("Enter a selection [1-3]"))


