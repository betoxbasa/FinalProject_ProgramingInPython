# Class used for management of the dataset with Pandas Library
# Author: Alberto Bautista
# import sys
# print(sys.path)

import pandas as pd
from IPython.display import display
from DataVisualization import DataVisualization


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

    #Get Sample of the data just first 10 rows
    def getInfoData(self):
        print(self.data.info())

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
            self.data = pd.read_csv("/Users/albertodavidbautistasanchez/Library/CloudStorage/OneDrive-Personal/Documentos/DataAnalytics/ProgrammingPython/FinalProject_ProgramingInPython/DataSet/airbnb_listings.csv")
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 

    #DataCleaning
    def PreDataCleaning(self):
        self.data['bathrooms_text'] = self.data['bathrooms_text'].str.split().str[0]
        self.data['bathrooms_text'] = pd.to_numeric(self.data['bathrooms_text'], errors='coerce').fillna(0.5)
        self.data['bathrooms_text'] = self.data['bathrooms_text'].astype(float)
        self.data['host_response_rate'] = self.data['host_response_rate'].str.replace('%', '')
        self.data["host_response_rate"].fillna(0, inplace=True)
        self.data['host_acceptance_rate'] = self.data['host_acceptance_rate'].str.replace('%', '')
        self.data["host_acceptance_rate"].fillna(0, inplace=True)
        self.data['first_review'] = pd.to_datetime(self.data['first_review'])
        self.data['last_review'] = pd.to_datetime(self.data['last_review'])
        self.data['calendar_last_scraped'] = pd.to_datetime(self.data['calendar_last_scraped'])

        self.data["host_response_rate"]=self.data["host_response_rate"].astype(int)
        self.data["host_acceptance_rate"]=self.data["host_acceptance_rate"].astype(int)

        self.data['price'] = self.data['price'].str.replace('$', '')
        self.data['price'] = self.data['price'].str.replace(',', '')
        self.data['price'] = self.data['price'].astype(float)

        host_response_time_dic = {
            "nan" :1,
            "a few days or more" :2,
            "within a day":3,
            "within a few hours":4,
            "within an hour":5
        }

        self.data['host_response_time'] = self.data['host_response_time'].astype(str).replace(host_response_time_dic)

        host_is_superhost_dic = {
            "t" :1,
            "f" :0    
        }

        self.data['host_is_superhost'] = self.data['host_is_superhost'].astype(str).replace(host_is_superhost_dic)
        self.data['host_has_profile_pic'] = self.data['host_has_profile_pic'].astype(str).replace(host_is_superhost_dic)
        self.data['host_identity_verified'] = self.data['host_identity_verified'].astype(str).replace(host_is_superhost_dic)
        self.data['has_availability'] = self.data['has_availability'].astype(str).replace(host_is_superhost_dic)
        self.data['instant_bookable'] = self.data['instant_bookable'].astype(str).replace(host_is_superhost_dic)
        self.data['host_is_superhost']

        # room_type_dic = {
        #     "Shared room" :1,
        #     "Private room" :2,
        #     "Hotel room":3,
        #     "Entire home/apt":4
        # }
        # self.data['room_type'] = self.data['room_type'].astype(str).replace(room_type_dic)
        self.data['description'] = self.data['description'].apply(lambda x: len(str(x).split()))
        columnasToDelete = ["listing_url","scrape_id","last_scraped","source","picture_url","host_url","host_thumbnail_url",
                    "host_picture_url","neighbourhood_group_cleansed","bathrooms","license","calendar_updated"]
        self.data.drop(columns=columnasToDelete, axis=0, inplace=True)
        self.data.drop(columns="host_about",axis=1,inplace=True)
        self.data.drop(columns="host_location",axis=1,inplace=True)
        self.data.drop(columns="host_neighbourhood",axis=1,inplace=True)
        self.data.drop(columns="neighborhood_overview",axis=1,inplace=True)
        self.data = self.data.dropna(subset=['review_scores_rating'])
        self.data = self.data.dropna(subset=['review_scores_value'])
        self.data = self.data.dropna(subset=['neighbourhood'])
        self.data = self.data.dropna(subset=['beds'])
        self.data = self.data.dropna(subset=['bedrooms'])
        self.data.dropna()
        #self.data.info()

        #DataVisualization
        


# myAirBnb = DataAirBnB()
# myAirBnb.PreDataCleaning()
# obj1 = DataVisualization()

# myAirBnb.getInfoData()
# myAirBnb.SubsetDataColumns("id","host_is_superhost")
# myAirBnb.SubsetDataRows(0, 3)
# myAirBnb.getSampleData()
# myAirBnb.ListColumns()
# myAirBnb.PrintColumn("id")
# myAirBnb.DescribeColumn("id")
#obj1.ShowHeatMapAll(myAirBnb.data)
# obj1.ShowHistogramAll(myAirBnb.data)
#obj1.ShowBoxPlotAll(myAirBnb.data,"price")
#obj1.ShowPairPlotAll(myAirBnb.data)



