# Class used for DataPloting of the dataset with Seaborn Library
# Author: Alberto Bautista
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self):
        self.Title = "AirBnb Plot Interface"

    def ShowHistogramAll(self, df):
        try:
            df.hist(figsize=(20,15))
            plt.show()
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 

    def ShowHeatMapAll(self,df):
        try:
            numeric = df[df.describe().columns]
            plt.figure(figsize=(30,15))
            sns.heatmap(numeric.corr(),annot=True, cmap="coolwarm", fmt='.2f')
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 
    
    def ShowBoxPlotAll(self,df,v1):
        try:
            df = df[df.describe().columns]
            fig = plt.figure(figsize=(20, 20))
            count = 0

            for variable in df.columns:
                count += 1
                plt.subplot(len(df), 1, count)
                ax = sns.boxplot(y=v1, x=variable, data=df)

            plt.tight_layout()
            plt.show()
        except Exception as e : 
                print(f"An unexpected error occurred: {e}") 
    
    def ShowPairPlotAll(self,df):
        try:
            # Create a pairplot
            sns.pairplot(df)
            plt.suptitle('Pairplot All Features', y=1.02)
            plt.show()
        except Exception as e : 
            print(f"An unexpected error occurred: {e}") 




