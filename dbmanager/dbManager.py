class dbManager:
	"""Db managment class"""
	
	path = ""

	def __init__(self, adapter):
		self.adapter = adapter
		self.adapter.connect()

	def __str__(self):
		return "This is dbManager with " + self.adapter 

	def add_row(self, tableName="", rowArray=[]):
		if not rowArray or not tableName:
			return
		self.adapter.add_row(tableName, rowArray)

	def commit(self):
		self.adapter.commit()

	def select_all(self, tableName=""):
		if not tableName:
			return
		yield from self.adapter.select_all(tableName)