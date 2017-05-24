import mysql.connector


class User():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3307,
                                database='people')
        self.cursor = self.conn.cursor()

    def insert(self, username, password):
        self._SQL = """insert into names
          (first_name, last_name)
          values
          (%s, %s)"""
        self.cursor.execute(self._SQL, (username, password))
        self.conn.commit()

    def query(self):
        flag = False
        query = ("""SELECT * FROM names WHERE first_name = %s""")
        name = input('Enter First name: ')
        self.cursor.execute(query, (name,))
        # print(len(self.cursor.execute(query, (name,))))
        print(self.cursor.rowcount)
        if not self.cursor.rowcount:
            print("No results found")
            print(flag)
        else:
            for row in self.cursor:
                print(row[0])
                flag = True
                print(flag)
        # for row in self.cursor.fetchall():
        #     print(row)
        #     name = row
        #     print(name)
        #     input()
        #     if name == ' ':
        #         print('Nothing found!')
        #     else:
        #         print(name)

# user = User()
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
