import os
import sqlite3

db_location = os.path.join(os.path.pardir(), 'hawksHistory.db') # lol, this should really be a runtime parameter
database_connection = sqlite3.connect(db_location)
