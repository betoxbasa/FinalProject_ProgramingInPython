# Class used for DataPloting of the dataset with Seaborn Library
# Author: Alberto Bautista
import pandas as pd
import seaborn as sns

class DataVisualization:
    def __init__(self):
        self.Title = "AirBnb Plot Interface"

    def ShowHistogram(self, df):
        df.hist(figsize=(30,15))



