################################################################
#
#   Main Street
#   CS146 19F Final Project
#   Kyla Barry, Julie (Min Jee) Cheon, Daniel Claro, Johnny Wong
#
################################################################
import sqlite3

DB_FILE = "data/street.db"

def create_db():
    '''Creates tables for DB_FILE'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    # replace these executes depending on necessary tables
    c.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS profiles (username TEXT PRIMARY KEY, hobbies TEXT, email TEXT, socials TEXT, phone TEXT)")

    db.close()
    return True

# create_db() # call this on initial creation of database

def get_users():
    '''Returns a dictionary containing all current users and corresponding passwords'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    cmd = 'SELECT username, password FROM users'
    c.execute(cmd)
    selectedVal = c.fetchall()

    db.close()
    return dict(selectedVal)

def find_user(username):
    '''Checks if username is unique'''
    users = get_users()
    return username in list(users.keys())

#########   NEED TO PROVIDE METHOD TO REGISTER PROFILE TOO!!! ####################
def register_user(username, password):
    '''Registers a user to the database'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    if find_user(username):
        return False
    else:
        c.execute('INSERT INTO users VALUES (?, ?)', (username, password))

        db.commit()
        db.close()
        return True

def verify_user(username, password):
    '''Checks if username and password matches those found in database'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute('SELECT username, password FROM users where username=?', (username,))

    selectedVal = c.fetchone()

    db.close()

    if selectedVal == None:
        return False
    elif username == selectedVal[0] and password == selectedVal[1]:
        return True
    return False

def add_profile(username, hobbies, email = "", socials = "", phone = ""):
    '''Adds profile to database. email, socials, and phone are optional parameters.'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    print(username)
    print(hobbies)
    print(email)
    print(socials)
    print(phone)
    c.execute('INSERT INTO profiles VALUES (?, ?, ?, ?, ?)', (username, hobbies, email, socials, phone))

    db.commit()
    db.close()
    return True

def get_profile(username):
    '''Returns dictionary of profile of user'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    c.execute('SELECT username, hobbies, email, socials, phone FROM profiles where username=?', (username,))

    selectedVal = c.fetchone()
    db.close()

    profile = {}
    profile['username'] = username
    profile['hobbies'] = selectedVal[1]
    profile['email'] = selectedVal[2]
    profile['socials'] = selectedVal[3]
    profile['phone'] = selectedVal[4]
    return profile

def find_friends(username, hobby):
    '''Returns a profile that contains an instance of <hobby>'''
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()

    query = '%' + hobby + '%'   # check if hobby is anywhere in the hobbies string on lookup
    c.execute('SELECT username, hobbies, email, socials, phone FROM profiles where hobbies LIKE ? AND username != ?', (query, username,))
    selectedVal = c.fetchall()
    db.close()
    return selectedVal
