#This file will hold the class that will manipulate the data from ufo.csv file.

#Importing files that will be used for the project
import csv
import geopandas as gpd
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from nvd3 import lineChart

#This class is what will handle all of the coding with the CSV file.
class Data():

    def __init__(self):
        self.__data = pd.read_csv('ufo.csv')

    #This method will return the number of UFO's by the state that the user IDed.
    def state_count(self, state):
        #Getting the state column
        states = self.__data[[3]]
        #Here I get the count of the number of ufo's by state
        count = len(states[states.State == state])
        #Returning the count
        return count

    #This method will return the number of UFO's by shape
    def shape_counter(self, shape):
        #Getting the Shape column
        shapes = self.__data[[2]]
        #Here I get the count of the number of ufo's by shape
        count = len(shapes[shapes.Shape_Reported == shape])
        #Returning the count
        return count

    #This method will return the number of UFO's by color
    def color_counter(self, color):
        #Focusing in on the colors column
        colors = self.__data[[1]]
        #Here I get the number of UFO's by color
        count = len(colors[colors.Colors_Reported == color])
        #Returning the count of UFO's by specific color
        return count

    #This method will return the number of UFO's by state and shape.
    def state_shape_counter(self, state, shape):
        #Notice how I save some lines and not seperating out the data first like I
        #did in the above three methods!
        count = len(self.__data[(self.__data.State == state) & (self.__data.Shape_Reported == shape)])
        return count

    #This method will return the number of UFO's by year.
    def year_count(self, year):
        #I have to convert the year to a string
        year_to_string = str(year)
        #Since my data has a full date instead of just the year, I need to ID
        #the values that contain my year.
        ufo_in_year = self.__data[self.__data.Time.str.contains(year_to_string)]
        #Getting the count of the UFO's in the year that the user specified.
        count = len(ufo_in_year)
        #Returning the value.
        return count

    #This method is not actually used in this project but I have included it here
    #because it is how I got the graph for the UFO count by year.
    def ufo_year_graph(self):
        value = "1930"
        count = int(value)
        years, date = [], []
        while count < 2001:
            test = self.__data[self.__data.Time.str.contains(value)]
            date.append(value)
            number = test.City.count()
            years.append(int(number))
            newValue = int(value)
            newValue += 1
            value = str(newValue)
            count += 1
        plt.plot(date, years, linewidth=2)
        plt.title("UFO Sightings By Year", fontsize=24)
        plt.xlabel("Year", fontsize=14)
        plt.ylabel("Count", fontsize=12)
        plt.show()

    #This method creates the graph of UFO sitings by year.
    def ufo_map(self):
        state_dict = {}
        self.__data = self.__data.groupby('State').size()
        count = 0
        while count < len(self.__data):
            state = self.__data.reset_index().values[count][0]
            value = self.__data.reset_index().values[count][1]
            state_dict[state] = value
            count += 1
        # with open('test.csv', 'w') as f:  # Just use 'w' mode in 3.x
        #     fieldnames = ['State', 'Value']
        #     w = csv.DictWriter(f, state_dict.keys())
        #     # w = csv.DictWriter(f, fieldnames=fieldnames)
        #     w.writeheader()
        #     w.writerow(state_dict)
        print(state_dict)

    #This method will allow the csv file to be used by D3.js.
    def convert_json_for_d3(self):
        # self.__data = pd.read_json('us-states.json')
        self.__data = gpd.read_file('us-states.json')
        df = self.__data
        return df

    #This method will allow me to build an interactive chart with nvd3 as oppossed
    #to the ufo_map method above.
    def nvd3_chart(self):
        value = "1930"
        count = int(value)
        years, date = [], []
        while count < 2001:
            test = self.__data[self.__data.Time.str.contains(value)]
            date.append(value)
            number = test.City.count()
            years.append(int(number))
            newValue = int(value)
            newValue += 1
            value = str(newValue)
            count += 1
        # Open File for test
        output_file = open('ufo_chart.html', 'w')
        #The rest of these lines will use NVD3 to create the graph.
        type = 'lineChart'
        chart = lineChart(name=type, height=600, width=600)
        #Creating the variables which will hold the data.
        xdata = date
        ydata = years
        kwargs1 = {'color': 'blue'}
        #This is what will actually plot the data
        chart.add_serie(y=ydata, name='UFO Count By Year', x=xdata, **kwargs1)
        #This builds the HTML file for my graph.
        chart.buildhtml()
        #Placing the D3 data into an HTML file.
        output_file.write(chart.htmlcontent)
        # close Html file
        output_file.close()

    #This method will allow the csv file to be used by D3.js.
    def convert_csv_for_d3(self):
        self.__data = pd.read_csv('test.csv')
        df = pd.DataFrame(self.__data)
        return df
