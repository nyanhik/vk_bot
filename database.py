import sqlite3

# https://pythonru.com/osnovy/sqlite-v-python
class repository: 
    __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cur = conn.cursor()