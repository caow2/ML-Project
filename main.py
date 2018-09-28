import sqlite3

db_file = 'data/ATLDataBase.db'
#db_file = 'ATL&PHL_Data_9_17_18_to_9_22_18/PHLDataBase.db'
conn = sqlite3.connect(db_file)

c = conn.cursor()

c.close()
