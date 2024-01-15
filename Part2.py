## Final Project - Python Programing 
## Student : Alberto David Bautista Sanchez
## 
## Part 2
## Interface for AirBnB
##
import os

def PrintSeparator():
    print("===================================================================")

def WelcomeMessage():
    PrintSeparator()
    print("            Welcome to AirBnB Interface to Explore Ireland")

def PrintMenu():
    PrintSeparator()
    ExploreDataLogic()

def ExploreDataLogic():
    PrintSeparator()
    print("1.- Show Sample of the data")
    print("2.- Get List of columns")
    print("3.- Select Columns")
    print("4.- Split the data")
    print("5.- Plots")
    print("6.- Describe of the data")
    print("Write 'Exit' to finish the program")

def main():
    os.system('clear')
    PrintSeparator()
    WelcomeMessage()

    PrintMenu()

    PrintSeparator()
    print("End Program")
    PrintSeparator()
    return

main()
    