import sqlite3

class sqlite3Adapter:
	"""docstring for sqlite3Adapter"""
	path = ""

	def __init__(self, pathToDb):
		self.path = pathToDb

	def connect(self):
		self.sqliteConnection = sqlite3.connect(self.path)
		self.sqliteCursor = self.sqliteConnection.cursor()

	def add_row(self, tableName="", rowArray=[]):
		self.sqliteCursor.execute("INSERT INTO " + tableName + " VALUES (" + str(rowArray)[1:-1] + ")")

	def commit(self):
		self.sqliteConnection.commit()

	def select_all(self, tableName=""):
		yield from self.sqliteCursor.execute("SELECT * FROM " + tableName)