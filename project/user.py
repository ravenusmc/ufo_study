#Importing files to use in this file.
import bcrypt
from bson.son import SON
import mysql.connector

class User():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3307,
                                database='user')
        self.cursor = self.conn.cursor()

    #This method will encrypt the password
    def encrypt_pass(self, password):
        password = password.encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        return password, hashed

    #This method will insert a new user into the database.
    def insert(self, username, hashed):
        self._SQL = """insert into users
          (username, password)
          values
          (%s, %s)"""
        self.cursor.execute(self._SQL, (username, hashed))
        self.conn.commit()

    def query(self):
        #I first encode the password to utf-8
        # password = password.encode('utf-8')
        query = ("""SELECT * FROM users WHERE username = %s""")
        name = input('Enter First name: ')
        self.cursor.execute(query, (name,))
        row = self.cursor.fetchone()
        if str(row) == 'None':
            print('NONE!')
            flag = False
        else:
            print(row[0] + ' ' + row[1])
            flag = True
            print(flag)
        # print("Row:",row)
        # print(len(self.cursor.execute(query, (name,)))) #Error Message
        # print(self.cursor.rowcount)
        # if not self.cursor.rowcount:
        #     print("No results found")
        #     print(flag)
        # else:
        #     for row in self.cursor:
        #         print(row[0])
        #         flag = True
        #         print(flag)

# user = User()
# user.insert('Abby', 4567)
# user.query()


    #This method will see if the user is actual user of the site.
    # def check(self, username, password):
    #     #I first encode the password to utf-8
    #     password = password.encode('utf-8')
    #     #I then search for a user that matches the username
    #     user = self.db.users.find_one({
    #         "username": username
    #     });
    #     #If user is not found then flag is set to False
    #     if str(user) == 'None':
    #         flag = False
    #     #If the user is found, then another check is done to see if the hidden
    #     #password matches the original one.
    #     else:
    #         #Setting the hashed variable to be used in the conditional statement.
    #         hashed = user['password']
    #         if bcrypt.hashpw(password, hashed) == hashed:
    #             #I don't believe I need this user real. I only need to return
    #             #the flag.
    #             user_real = self.db.users.find_one({
    #                 "username": username,
    #                 "password": password
    #             });
    #             flag = True
    #     return flag
