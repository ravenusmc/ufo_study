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

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
        #Recieving the information from the form from the user.
        username = request.form['username']
        password = request.form['password']
        #Creating the object that will represent the user.
        user = User()
        #Now checking to see if the user is in the database.
        flag = user.check(username, password)
    #     #Conditional statement to test if the user is a member of the site.
    #     if flag == True:
    #         #If the user is in the database, the user gets sent to the index page.
    #         session['username'] = request.form['username']
    #         #Sending the user to the index page
    #         return redirect(url_for('index'))
    #     else:
    #         #If the user is not in the database then they will be sent to the
    #         #sign up page.
    #         return redirect(url_for('sign_up'))
    return render_template('login.html', title='Login Page')

@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')

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


# set the secret key. keep this really secret:
app.secret_key = 'n3A\xef(\xb0Cf^\xda\xf7\x97\xb1x\x8e\x94\xd5r\xe0\x11\x88\x1b\xb9'

#This line will actually run the app.
if __name__ == '__main__':
    app.run(debug=True)
