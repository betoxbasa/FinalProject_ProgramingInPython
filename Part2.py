## Final Project - Python Programing 
## Student : Alberto David Bautista Sanchez
## 
## Part 2
## Interface for AirBnB
##
import os
from DataSetManagement import DataSetManagement
from DataSetManagement import DataVisualization

def PrintSeparator():
    print("===================================================================")

def WelcomeMessage():
    PrintSeparator()
    print("            Welcome to AirBnB Interface to Explore Ireland")

def PrintMenu():
    PrintSeparator()
    ExploreDataLogic()

def LogicSegmentation(ds):
    StartColumn = input("Insert Start Column Name : ")
    EndColumn = input("Insert End Column Name : ")
    ds.SubsetDataColumns(StartColumn,EndColumn)

def LogicPlot(ds):
    PrintSeparator()
    dv = DataVisualization.DataVisualization()
    response2=""
    while(response2!="Exit") :
        print("1.- HistogramAll")
        print("2.- HeatMapAll")
        print("3.- BoxPlotAllbyColumn")
        print("4.- Show Pair Plot All")
        print("Write 'Exit' to finish the program")
        response2 = input("Write your response : ")

        if response2 == '1':
            dv.ShowHistogramAll(ds)
        elif response2 == '2':
            dv.ShowHeatMapAll(ds)
        elif response2 == '3':
            variableVs = input("Insert Name of column to compare :")
            dv.ShowBoxPlotAll(ds,variableVs)
        elif response2 == '4':
            dv.ShowPairPlotAll(ds)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    

def ExploreDataLogic():
    PrintSeparator()
    print("1.- Show Sample of the data")
    print("2.- Get List of columns")
    print("3.- Select Columns")
    print("4.- Split the data")
    print("5.- Plots")
    print("Write 'Exit' to finish the program")

def main():
    response = ""
   # os.system('clear')
    while(response!="Exit"):
        PrintSeparator()
        WelcomeMessage()
        mydata = DataSetManagement.DataAirBnB()
        mydata.PreDataCleaning()
        PrintMenu()
        response = input("Write your option : ")
        print("Inicio de logic")
        if response == '1':
            mydata.ShowAllData()
        elif response == '2':
            mydata.ListColumns()
        elif response == '3':
            LogicSegmentation(mydata)
            mydata.ShowAllData()
        elif response == '4':
            mydata.ShowAllData()
        elif response == '5':
            LogicPlot(mydata.data)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

        PrintSeparator()
        print("End Program")
        PrintSeparator()
    return

main()
    