import sys
import os

def mainMenu():
    print("\n\t\t\t~`~`~`~`~`~CONVERSION MACHINE~`~`~`~`~`~\t\t\n")
    selection = int(input("Select the choice you want to convert[1-3]\nSelection:\n1. Centimeters\n2. Inches\n3. Feet\n4. End Program"))

    print("Selection:\n1. Centimeters\n2. Inches\n3. Feet\n4. End Program")
    #print("1. Centimeters\n2. Inches\n3. Feet\n4. End Program")

    if (selection == 4):
        print("Thanks for using my Conversion Machine!")
        sys.exit()
    selection2 = int(input("Select the choice you want to convert to [1-3]\n"))

    if (selection == 1) and (selection2 == 2):
        centTOin()
    elif (selection == 1) and (selection2 == 3):
        centTOft()
    elif (selection == 2) and (selection2 == 1):
        inTOcent()
    elif (selection == 2) and (selection2 == 3):
        inTOft()
    elif (selection == 3) and (selection2 == 1):
        ftTOcent()
    elif (selection == 3) and (selection2 == 2):
        ftTOin()
    elif selection == selection2:
        val = int(input("What number would you like to convert?\n"))
        print(val,"is your conversion")
        
        
    
        
        
        


def centTOin():
    val = int(input("How many centimeters do you have?(cent to inches)"))
    convert = (val * 0.393701)
    print(val, "centimeters is",convert,"inches")
    exite = input("Would you like to try again?[Y/N]\n")
    
    if (exite == "Y") or (exite == "y"):
        centTOin()
    elif exite == "n" or exite == "N":
        mainMenu()
        
def centTOft():
    val = int(input("How many centimeters do you have? (centimeters to feet)"))
    convert = (val * 0.0328084)
    print(val, "centimeters is",convert,"feet")
    exite = input("Would you like to try again?[Y/N]\n")

    if (exite == "Y") or (exite == "y"):
        centTOft()
    elif exite == "n" or exite == "N":
        mainMenu()
def inTOcent():
    val = int(input("How many inches do you have?(inches to cent)"))
    convert = (val * 2.54)
    print(val, "inches is",convert,"centimeters")
    exite = input("Would you like to try again?[Y/N]\n")
    
    if exite == "Y" or exite == "y":
        inTOcent()
    elif exite == "n" or exite == "N":
        mainMenu()
def inTOft():
    val = int(input("How many inches do you have?(inches to feet)"))
    convert = (val / 12)
    print(val, "inches is",convert,"feet")
    exite = input("Would you like to try again?[Y/N]\n")

    if (exite == "Y") or (exite == "y"):
        inTOft()
    elif exite == "n" or exite == "N":
        mainMenu()
def ftTOcent():
    val = int(input("How many feet do you have? (feet to centimeters)"))
    convert = (val * 30.48000097536)
    print(val, "feet is",convert,"centimeters")
    exite = input("Would you like to try again?[Y/N]\n")

    if (exite == "Y") or (exite == "y"):
        ftTOcent()
    elif exite == "n" or exite == "N":
        mainMenu()
def ftTOin():
    val = int(input("How many feet do you have? (feet to inches)"))
    convert = (val * 12)
    print(val, "feet is",convert,"inches")
    exite = input("Would you like to try again?[Y/N]\n")

    if (exite == "Y") or (exite == "y"):
        ftTOin()
    elif exite == "n" or exite == "N":
        mainMenu()
        
mainMenu()
