import sqlite3

class Sqlite3:
	"""docstring for sqlite3Adapter
		
		now this class is signature influenced in cause of add_row(...) function.

	"""
	_path = ""
	_idColumnName =""

	def __init__(self, pathToDb, idColumnName):
		self._path = pathToDb
		self._idColumnName = idColumnName

	def connect(self):
		self.sqliteConnection = sqlite3.connect(self._path)
		self.sqliteCursor = self.sqliteConnection.cursor()

	def add_row(self, tableName="", rowArray=[]):
		self.sqliteCursor.execute("INSERT INTO " + tableName + " (name, count, price) VALUES (" + str(rowArray)[1:-1] + ")")

	def delete(self, tableName="", idArray=[]):
		self.sqliteCursor.execute("DELETE FROM " + tableName + " WHERE " + self._idColumnName + " IN (" + str(idArray)[1:-1] + ") ")

	def decrease(self, idArray=[]):
		if not idArray:
			return
		self.adapter.decrease(idArray)

	def reserve(self, idArray=[]):
		if not idArray:
			return
		self.adapter.reserve(idArray)

	def update(self, id, rowArray=[]):
		if not rowArray or (id < 0):
			return
		self.adapter.update(id, rowArray)


	def commit(self):
		self.sqliteConnection.commit()

	def select_all(self, tableName=""):
		yield from self.sqliteCursor.execute("SELECT * FROM " + tableName)