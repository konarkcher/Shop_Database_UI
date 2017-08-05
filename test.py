from dbmanager import dbManager
from dbmanager import sqlite3Adapter

sql3Adpt = sqlite3Adapter.sqlite3Adapter("db/test.db") 
db = dbManager.dbManager(sql3Adpt)


# Create table
sql3Adpt.sqliteCursor.execute('''CREATE TABLE stocks
             (id int,date text, trans text, symbol text, qty real, price real)''')

sql3Adpt.sqliteCursor.execute("CREATE UNIQUE INDEX stoks_ind ON stocks (id)")

# Insert a row of data
db.add_row("stocks",[1,'2006-01-05','BUY','RHAT0',100,35.14])
db.add_row("stocks",[2,'2006-01-05','BUY','RHAT1',100,35.14])
db.add_row("stocks",[3,'2006-01-05','BUY','RHAT2',100,35.14])
db.add_row("stocks",[4,'2006-01-05','BUY','RHAT3',100,35.14])

# Save (commit) the changes
db.commit()

for row in db.select_all("stocks"):
	print(row)

sql3Adpt.sqliteCursor.execute("DELETE FROM stocks")

sql3Adpt.sqliteCursor.execute("DROP TABLE stocks")

sql3Adpt.sqliteConnection.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
sql3Adpt.sqliteConnection.close()