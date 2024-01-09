import pandas as pd

class DataAirBnB:
    def __init__(self):
        self.data = pd.read_csv("airbnb_listings.csv")

    def getRows(self):
        print(self.data.shape)

myAirBnb = DataAirBnB()
myAirBnb.getRows()

# dataframe = pd.read_csv("airbnb_listings.csv")