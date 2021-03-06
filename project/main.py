#importing outside libraries for use in the project
from flask import Flask, session, jsonify, redirect, url_for, escape, render_template, request, flash
import matplotlib.pyplot as plt, mpld3
import numpy as np
import pandas as pd

#importing files that I made for this project
from ufo import *
from user import *

#Setting up Flask
app = Flask(__name__)

#This function brings the user to the login page.
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Recieving the information from the form from the user.
        username = request.form['username']
        password = request.form['password']
        #Creating the object that will represent the user.
        user = User()
        #Now checking to see if the user is in the database.
        flag = user.check(username, password)
        #Conditional statement to test if the user is a member of the site.
        if flag == True:
            #If the user is in the database, the user gets sent to the index page.
            session['username'] = request.form['username']
            #Sending the user to the index page
            return redirect(url_for('home'))
        else:
            #If the user is not in the database then they will be sent to the
            #sign up page.
            return redirect(url_for('signup'))
    return render_template('login.html', title='Login Page')

#This function brings the user to the sign in page.
@app.route('/signin', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        #Recieving the information from the form from the user.
        username = request.form['username']
        password = request.form['password']
        #Creating the object that will represent the user.
        user = User()
        #Encrypting the password
        password, hashed = user.encrypt_pass(password)
        #Adding the user to the database
        user.insert(username, hashed)
        #Letting them into the index Page
        return redirect(url_for('home'))
    return render_template('sign_in.html', title='sign_in')

#This function will bring the user to the home page
@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', title='Home Page')


#This function will bring the user to the graph page
@app.route('/graph')
def graph():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('graph.html', title='Graph Page')

#This function will bring the user to the data page
@app.route('/data')
def data():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('data.html', title='Data Page')

#This function is what will convert a csv file to be used with d3.
@app.route('/my/data/endpoint')
def get_d3_data():
    data = Data()
    data_file = data.convert_csv_for_d3()
    return data_file.to_csv()

#This function is what will log out the user.
@app.route('/sign_out')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

#AJAX Functions here.

#This function looks at UFOs by state
@app.route('/_by_state')
def by_state():
    #Creating an object that will be used to analyze data by the year
    data = Data()
    #pulling the data from what the user entered
    state = request.args.get('state', 0, type=str)
    #Capitalizing the state name to ensure that it matches what is in the csv file
    state = state.upper()
    #Using the state_count method from the ufo.py file to find the number of
    #UFO's by state.
    count = data.state_count(state)
    #Returning the state count back to the user.
    return jsonify(result = count)

#This function looks at UFO's by shape
@app.route('/_by_shape')
def by_shape():
    #Creating an object that will be used to analyze data by the shape
    data = Data()
    #Receiving the data from what the user entered
    shape = request.args.get('shape', 0, type=str)
    #I have to uppercase all letters in shape since that is how the data is in
    #the csv
    shape = shape.upper()
    count = data.shape_counter(shape)
    return jsonify(result = count)

@app.route("/json")
def json():
    data = Data()
    data_file = data.convert_json_for_d3()
    # return data_file
    return data_file.to_json()
    # return jsonify(get_data())

#This function looks at UFO's by color
@app.route('/_by_color')
def by_color():
    #Creating an object that will be used to analyze data by the color
    data = Data()
    #Receiving the data from what the user entered
    color = request.args.get('color', 0, type=str)
    #I have to convert the color string to all uppercase for the csv file.
    color = color.upper()
    count = data.color_counter(color)
    return jsonify(result = count)

#This function looks at UFO's by state and shape
@app.route('/_by_state_shape')
def by_state_shape():
    #Creating an object that will be used to analyze data by the color
    data = Data()
    state = request.args.get('state_two', 0, type=str)
    shape = request.args.get('shape_two', 0, type=str)
    #Capitalizing the state and shape name to ensure that it matches what is in the csv file
    state = state.upper()
    shape = shape.upper()
    count = data.state_shape_counter(state, shape)
    return jsonify(result = count)

#This function looks at the count of UFO's by year
@app.route('/_by_year')
def by_year():
    #Creating an object that will be used to analyze data by the year
    data = Data()
    year = request.args.get('year', 0, type=int)
    #Calling the year_count method from the Data class to get the number of UFO's by year.
    count = data.year_count(year)
    return jsonify(result = count)

#END OF AJAX FUNCTIONS

# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)
