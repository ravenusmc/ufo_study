#This file will hold the class that will manipulate the data from ufo.csv file.

#Importing files that will be used for the project
import numpy as np
import pandas as pd

class Data():

    def __init__(self):
        self.__data = pd.read_csv('ufo.csv')

    def state(self):
        print(self.__data.head())

data = Data()
data.state()
