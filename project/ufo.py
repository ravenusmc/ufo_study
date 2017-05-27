#This file will hold the class that will manipulate the data from ufo.csv file.

#Importing files that will be used for the project
import numpy as np
import pandas as pd

#This class is what will handle all of the coding with the CSV file.
class Data():

    def __init__(self):
        self.__data = pd.read_csv('ufo.csv')

    #This method will return the number of UFO's by the state that the user IDed.
    def state_count(self, state):
        #Getting the state column
        states = self.__data[[3]]
        count = len(states[states.State == state])
        return count

# data = Data()
# data.state()
