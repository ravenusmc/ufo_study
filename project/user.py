import mysql.connector


class User():

    def __init__(self):
        self.conn = mysql.connector.connect(user='ted',
                                password='pass',
                                host='localhost',
                                port=3307,
                                database='people')
        self.cursor = self.conn.cursor()

    def insert(self):
        self._SQL = """insert into names
          (first_name, last_name)
          values
          (%s, %s)"""
        f_name = input('Enter a First name: ')
        l_name = input('Enter a last name: ')
        self.cursor.execute(self._SQL, (f_name, l_name))
        self.conn.commit()

user = User()
user.insert()
