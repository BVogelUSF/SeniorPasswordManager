import datetime
import pyodbc


# Standardized Query function, cursor is generated for pyodbc and account is generated through
# account creation, all other variables are user input
# returns Ouput, which will either be the error message or the password
def query(cursor, login, password, website, username, account):
    try:
        cursor.execute(""
                       "OPEN SYMMETRIC KEY " + login + "Key\n"
                       "DECRYPTION BY CERTIFICATE " + login + "Certificate\n"
                       "WITH PASSWORD = '" + password + "';")
        conn.commit()
    except pyodbc.ProgrammingError:
        output = "How did you even break this?"
        return output
    finally:
        cursor.execute("CLOSE SYMMETRIC KEY " + login + "Key")
        conn.commit()

    # Process to first open the User's unique encryption key. No errors should occur as this is verified
    # through login. Second task begins at UPDATE, User's data is decrypted for querying.
    try:
        cursor.execute("OPEN SYMMETRIC KEY " + login + "Key "
                       "DECRYPTION BY CERTIFICATE " + login + "Certificate "
                       "WITH PASSWORD = '" + password + "';"
                       "UPDATE UserPasswords\n"
                       "set Pass = CONVERT(varchar(1000), DECRYPTBYKEY(Pass)),"
                       "Website = CONVERT(varchar(1000), DECRYPTBYKEY(Website)),"
                       "Username = CONVERT(varchar(1000), DECRYPTBYKEY(Username))"
                       "WHERE UserID = '" + account + "';")
        conn.commit()
    except pyodbc.ProgrammingError:
        output = "How did you even break this?"
        return output
    # Query line, selects password based on website and username. Written to use SQL Parameters to make it
    # resistant to SQL Injection
    cursor.execute("SELECT Pass FROM UserPasswords WHERE Website = ? AND Username = ?", (website,username))
    # Verifies if a password exists and then re-encrypts the data and closes the key
    try:
        row = cursor.fetchone()
        output = row[0]
    except TypeError:
        output = "No password found"
    finally:
        cursor.execute(""
                       "OPEN SYMMETRIC KEY " + login + "Key "
                       "DECRYPTION BY CERTIFICATE " + login + "Certificate "
                       "WITH PASSWORD = '" + password + "';"
                       "UPDATE UserPasswords\n"
                       "SET Pass = ENCRYPTBYKEY(Key_GUID('" + login + "Key'),Pass),"
                       "Username = ENCRYPTBYKEY(Key_GUID('" + login + "Key'),Username),"
                       "Website = ENCRYPTBYKEY(Key_GUID('" + login + "Key'),Website)"
                       "WHERE UserID = '" + account + "';")
        conn.commit()
        cursor.execute("CLOSE SYMMETRIC KEY " + login + "Key")
        conn.commit()
    return output


# Standardized Insert query, as with Query, cursor and account are generated by system while rest are user input
# No return value
def insert(cursor, login, password, insPassword, website, username, account):
    try:
        cursor.execute(""
                       "OPEN SYMMETRIC KEY " + login + "Key\n"
                       "DECRYPTION BY CERTIFICATE " + login + "Certificate\n"
                       "WITH PASSWORD = '" + password + "';")
        conn.commit()
    except pyodbc.ProgrammingError:
        output = "How did you even break this?"
        return output
    finally:
        cursor.execute("CLOSE SYMMETRIC KEY " + login + "Key")
        conn.commit()
    # The insert statement, designed to use SQL parameters to make it resistant to SQL Injection
    cursor.execute("INSERT INTO UserPasswords VALUES (?,?,?,?)",(insPassword,account,website,username))
    conn.commit()
    # Update statement for encryption, first opens the User's unique key then encrypts the data
    cursor.execute(""
                   "OPEN SYMMETRIC KEY " + login + "Key "
                   "DECRYPTION BY CERTIFICATE " + login + "Certificate "
                   "WITH PASSWORD = '" + password + "';"
                   "UPDATE UserPasswords\n"
                   "SET Pass = ENCRYPTBYKEY(Key_GUID('" + login + "Key'),Pass),"
                   "Username = ENCRYPTBYKEY(Key_GUID('" + login + "Key'),Username),"
                   "Website = ENCRYPTBYKEY(Key_GUID('" + login + "Key'),Website)"
                   "WHERE Username = '" + username + "';")
    conn.commit()
    cursor.execute("CLOSE SYMMETRIC KEY " + login + "Key")
    conn.commit()


# The function that creates accounts, requires the user to enter a login and passcode
# returns output, which is either error text or the UserID
def createAccount(cursor,login,password):
    joinDate = str(datetime.date.today())
    output = ""
    # Tests to see if the username is taken, if the query returns a value the username is taken,
    # if an exception occurs it means that the query returned Null, so the username is free
    try:
        cursor.execute(""
                       "SELECT AccountID FROM Accounts\n"
                       "WHERE AccountName = '" + login + "'")
        row = cursor.fetchone()
        output = row[0]
    except TypeError:
        conn
    else:
        output = "Username already exists"
        return output
    # attempts certificate creation, validates password integrity in the process
    try:
        cursor.execute(""
                       "CREATE CERTIFICATE " + login + "Certificate\n"
                       "ENCRYPTION BY PASSWORD = '" + password + "'\n"
                       "WITH SUBJECT = '" + login + "Certificate'\n")
        conn.commit()
    # password policy dictates a password of at least 8 characters with 1 uppercase, 1 lowercase, and 1 complex
    # character
    except pyodbc.ProgrammingError:
        if len(password) < 8:
            output = "Password isn't long enough"
        elif len(password) > 255:
            output = "Password is too long"
        else:
            output = "Password isn't complex enough, requires at leas 1 Uppercase letter1 complex character and 1" \
                     " lowercase letter"

        return output
    # creation of unique key if certificate is successful
    cursor.execute(""
                   "CREATE SYMMETRIC KEY " + login + "Key\n"
                   "WITH ALGORITHM = AES_128\n"
                   "ENCRYPTION BY CERTIFICATE " + login + "Certificate")
    conn.commit()
    # creates the user's UserID and logs their account
    cursor.execute(""
                   "INSERT INTO Accounts (AccountName, JoinDate)\n"
                   "VALUES ('" + login + "','" + joinDate + "');")
    conn.commit()
    # returns their new UserID
    cursor.execute(""
                   "SELECT AccountID FROM Accounts\n"
                   "WHERE AccountName = '" + login + "'")
    row = cursor.fetchone()
    output = row[0]
    return output


# Login function, requires user input of login and password
# returns either error text or UserID
def login(cursor, login, password):
    # attempts query for username, returns error if query returns null
    try:
        cursor.execute(""
                       "SELECT AccountID FROM Accounts\n"
                       "WHERE AccountName = '" + login + "'")
        row = cursor.fetchone()
        output = row[0]
    except TypeError:
        output = "Username doesn't exist"
        return output
    # attempts login to existing user, returns error if password doesn't match
    try:
        cursor.execute(""
                       "OPEN SYMMETRIC KEY " + login + "Key\n"
                       "DECRYPTION BY CERTIFICATE " + login + "Certificate\n"
                       "WITH PASSWORD = '" + password + "';")
        conn.commit()
    except pyodbc.ProgrammingError:
        output = "Password incorrect"
        return output
    cursor.execute("CLOSE SYMMETRIC KEY " + login + "Key")
    conn.commit()
    return output


server = 'cadebrodyproject.database.windows.net'
database = 'PasswordManager'
username = 'azureuser'
password = '2XzmEYVgA5XVCH7'
driver= '{ODBC Driver 18 for SQL Server}'

# the connection string for accessing the database, don't change any of the values without asking
# tends to break
conn = pyodbc.connect(''
                      'DRIVER='+driver +
                      ';SERVER=tcp:'+server +
                      ';PORT=1433;'
                      'DATABASE='+database +
                      ';UID='+username +
                      ';PWD=' + password)

cursor = conn.cursor()
# username = "finaltest"
# password = "passwordTest!!"
# website = "www.Windows.com"
# name = "CadePrice"
# genPassword = "totallydifferentpassword"
# account = login(cursor,username,password)
# print(account)
# insert(cursor,username,password,genPassword,website,name,account)
# long = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" \
#        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# print(len(long))
# print(createAccount(cursor,username,long))


# print(query(cursor,username,password,website,name,str(account)))
# password = "wrong"






# Test code begins here:

# user inputs for their login and password
logName = "finaltest2"
logPass = "passwordTest!!"

# Login function runs, verifies the login information
# returns userID which is their id in the database
userID = login(cursor,logName,logPass)
userID = str(userID)
# if you want to verify the database functions for you
# run the print and comment out everything below it
print(userID)

# # user input
# username1 = "Vogel1"
# website1 = "www.test.com"
# pass1 = "testtesttest"
#
# # inserts the data into the database then encrypts it
# insert(cursor,logName,logPass,pass1,website1,username1,userID)
#
# # data sent to function, returns as string
# queryReturn1 = query(cursor,logName,logPass,website1,username1,userID)
# print(queryReturn1)
#
# # same as above, but new inputs
# username1 = "Vogel2"
# website1 = "www.gmail.com"
# pass1 = "thisisntsecure"
#
# insert(cursor,logName,logPass,pass1,website1,username1,userID)
# queryReturn1 = query(cursor,logName,logPass,website1,username1,userID)
# print(queryReturn1)