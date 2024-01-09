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
    print("1.-Give me insights regarding airbnbs")
    print("2.-Explore the data")
    print("3.-Exit")

def PrintMenuInsights():
    print("1.-Give me the top 10 rated Airbnb’s where I can stay at least 8 nights and is instantly bookable")
    print("2.-Plot the host response rate against the host response time in a scatter plot ")
    print("3.-Show me the amount of Airbnb’s in Dublin, Ireland which have a cleanliness rating higher than 4.0")
    print("4.-Provide the cleanliness rating scores for listings 12-15")
    print("5.-Return Menu")

def ExploreDataLogic():
    PrintSeparator()
    print("1.- Show Sample of the data")
    print("2.- Get List of columns")
    print("3.- Select Columns")
    print("4.- Split the data")
    print("5.- Plots")
    print("6.- Describe of the data")

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
    