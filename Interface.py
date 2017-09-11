import sqlite3

#GLOBAL CONNECT
CONNECTION = None
CURSOR = None
DEBUG = False

# Connect to the database
# If filename is not present in path it will be created.
# Defines the global cursor
def connect(filename, isRAM):
    # This creates an optional DB in RAM
    if isRAM:
        conn = sqlite3.connect(':memory:')
    else:
        conn = sqlite3.connect(filename)
    #set the cursor object
    global CURSOR
    global CONNECTION
    CONNECTION = conn
    CURSOR = conn.cursor()


# Creating a DB table
# Expects a name and dictionary of columns mapped to their data types
def createTable(tablename, columns):
    cmd = "CREATE TABLE "+ tablename +" ("
    for key in columns.keys():
        cmd += key + " " + columns.get(key) + ","
    cmd = cmd[:-1]
    cmd += ")"
    try:
        if DEBUG: print(cmd)
        CURSOR.execute(cmd)
    except sqlite3.OperationalError as e:
        print("ERROR! " + str(e))


# Insert data row
# Expects the table name and the array of values to insert
def insertRow(tablename, values):
    cmd = "INSERT INTO "+tablename+" VALUES ("
    for v in values:
        if type(v) == str:
            cmd += '''"'''+ v + '''"''' + ","
        else:
            cmd += str(v) + ","
    cmd = cmd[:-1]
    cmd += ")"
    try:
        if DEBUG: print(cmd)
        CURSOR.execute(cmd)
        #save changes
        CONNECTION.commit()
    except sqlite3.OperationalError as e:
        print("ERROR! " + str(e))


# Dump the whole DB ordered by a column
def dump(tablename, orderbase):
    dump = []
    cmd = 'SELECT * FROM '+ tablename +' ORDER BY '+orderbase
    if DEBUG: print(cmd)
    for row in CURSOR.execute(cmd):
        dump.append(row)
    return dump