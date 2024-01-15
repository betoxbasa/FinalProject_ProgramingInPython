# Class used for management of the dataset with Pandas Library
# Author: Alberto Bautista
# import sys
# print(sys.path)

import pandas as pd
from IPython.display import display
from DataVisualization import DataPloting

#Constructor
class DataAirBnB:
    def __init__(self):
        try:
            self.data = pd.read_csv("/Users/albertodavidbautistasanchez/Library/CloudStorage/OneDrive-Personal/Documentos/DataAnalytics/ProgrammingPython/FinalProject_ProgramingInPython/DataSet/airbnb_listings.csv")
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 

    #Get Sample of the data just first 10 rows
    def getSampleData(self):
        print(self.data.head(10))

    #Show all data into the data frame.
    def ShowAllData(self):
        print(self.data)

    #Show a list of all columns of the dataframe.
    def ListColumns(self):
        for index,row in enumerate(self.data.columns):
            print(f"{index} {row}")

    #Show Data from one column.
    def PrintColumn(self, ColumnName):
        try:
            for index,row in enumerate(self.data[ColumnName]):
                print(f"{index} {row}")
        except Exception as e : 
            print(f"An unexpected error occurred: {e}")

    #Show Columns by number of column.
    def PrintColumnByNumber(self, Num):
        try:
            for index,row in enumerate(self.data.iloc[:, Num]):
                print(f"{index} {row}")
        except Exception as e : 
            print(f"An unexpected error occurred: {e}")
    
    #Show Statistical Data of the datafram.
    def DescribeData(self):
        display(self.data.describe())

    #Show Statistical Data of one column.
    def DescribeColumn(self,ColumnName):
        try:
            print(self.data[ColumnName].describe())
        except Exception as e : 
            print(f"An unexpected error occurred: {e}")

    #Generate a subDataframe in a range of columns by name.
    def SubsetDataColumns(self,StartColumn,EndColumn):
        try:
            self.data=self.data.loc[:,StartColumn:EndColumn]
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 
    
    #Generate a subDataframe in a range of number of rows.
    def SubsetDataRows(self,StartRow,EndRow):
        try:
            self.data = self.data.loc[StartRow:EndRow, :]
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 

    #Generate a subDataframe with a list of columns.
    def SelectColumns(self,ColumnNames):
        try:
            self.data = self.data[ColumnNames]
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 

    #Reload the original dataframe from csv file.
    def ResetData(self):
        try:
            self.data = pd.read_csv("DataSetManagement/airbnb_listings.csv")
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 
        


myAirBnb = DataAirBnB()

obj1 = DataPloting()
obj1.ShowHistogram(myAirBnb.data)
myAirBnb.ShowAllData()
# myAirBnb.SubsetDataColumns("id","last_scraped")
# myAirBnb.SelectColumns(["id","scrape_id","zzz"])
# myAirBnb.SubsetDataRows(0, 3)
# myAirBnb.getSampleData()
#myAirBnb.ListColumns()
#myAirBnb.PrintColumn("id")
#myAirBnb.DescribeColumn("id")
# dataframe = pd.read_csv("airbnb_listings.csv")
        
