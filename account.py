import mysql.connector
from mysql.connector import Error

def __main__():

    mainCycle = True
    while mainCycle == True:

        try:
            print("1. Login")
            print("2. Register")
            option = int(input("Your selection: "))
            if option == 1 or option == 2:
                mainCycle = False
            else:
                raise IndexError
        except ValueError:
            print("Must be a whole number")
        except IndexError:
            print("Either 1 or 2")
        except KeyboardInterrupt:
            print("Bye")
            quit()
        except TypeError:
            print("Invalid input")
        except:
            print("Something else went wrong")

    if option == 1:
        User.login(self=None)
    elif option == 2:
        User.register(self=None)

def servConnection():
    server = mysql.connector.connect(
        host="192.168.56.9",
        user="thisisme",
        password="thisisme",
        database="Account")
    return server

### User class, user can either login or register
class User():

    def login(self):

        username = input("Username: ")
        password = input("Password: ")

        try:
            servConnection()
        except mysql.connector.Error as error:
            print("Connection failed ", error)
            quit()
        else:
            print("Connection established")
            server = servConnection()

        cursor = server.cursor() # cursor establishment
        # Need to verify the found values
        query1 = """SELECT username FROM Users WHERE username = '%s'""" % (username)
        cursor.execute(query1)

        for row in cursor.fetchall(): # reads the cursors
            storedUser = row[0] # stores the value in variable

        try:
            if len(row) > 0:
                print(storedUser+" in the database")
            else:
                raise Exception
        except Exception:
            print("not in the database")


    def register(self):

        while True: # Username loop
            username = input("Username: ")
            if len(username) >= 4:
                break
            else:
                print("Has to be at least 4 characters long")

        while True: # Password loop
            password1 = input("Password: ")
            password2 = input("Password again: ")

            if password1 == password2:
                password = password1
                if len(password) >= 8:
                    break
                else:
                    print("Has be at least 8 characters long")
            else:
                print("Passwords do not match")

        SendCredentials(username, password)


### checks the connection and sends data ###
class SendCredentials:

    def __init__(self, username, password):
        # check the connection
        try:
            servConnection()
            server = servConnection()
        except mysql.connector.Error as error:
            print("Connection failed ", error)
            quit()
        else:
            cursor = server.cursor() # cursor establishment
            print("Connection established")

        verifyUser = """SELECT username FROM Users WHERE username = '%s'""" % (username)
        cursor.execute(verifyUser)
        try:
            for row in cursor.fetchall(): # reads the cursors
                storedUser = row[0] # stores the value in variable
            if len(row) > 0:
                print(storedUser+" username is already taken")

        except UnboundLocalError:
            command = "INSERT INTO Users (username, password) VALUES (%s, %s)"
            values = (username, password)
            cursor.execute(command, values)
            server.commit()
            print("Values sent successfully")
            cursor.execute("SELECT * FROM Users")
            for row in cursor.fetchall():
                print (row)

        print("Bye")
        quit()

if __name__ == '__main__': # code cannot be imported from elsewhere
    __main__()
