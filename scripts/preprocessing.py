import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler


class Data_preprocessing:
    def __init__(self):
        pass

    def datetime(self,df,column):
        df[column] = pd.to_datetime(df[column])
        return df[column]

    def numeric(self,df,column):
        df[column]= pd.to_numeric(df[column])
        return df[column]

    def fill_ffill(self,df,column):
        df[column] = df[column].fillna(method='ffill')
        return df[column]

    def fill_bfill(self,df,column):
        df[column] = df[column].fillna(method='bfill')
        return df[column]

    def fill_mean(self,df,column):
        df[column] = df[column].fillna(df[column].mean())
        return df[column]

    def fill_mode(self,df,column):
        df[column] = df[column].fillna(df[column].mode())
        return df[column]

    def label_encode(self,df,column):
        df[column] = LabelEncoder().fit_transform(df[column])
        return df[column]

    def scale_data(self,df):
        df = StandardScaler().fit_transform(df)
        return df
