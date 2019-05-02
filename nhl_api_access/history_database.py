import os
import sqlite3

# This should really be a class, and the DB should be safely closed, it isn't rn
db_location = os.path.join(os.path.pardir, "hawksHistory.db")  # lol, this should really be a runtime parameter
database_connection = sqlite3.connect(db_location)
