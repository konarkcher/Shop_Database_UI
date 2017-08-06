import sqlite3


class Sqlite3:
    """
    docstring for sqlite3Adapter
        
    now this class is signature influenced in cause of add_row(...) function.

    """
    _path = ""
    _id_column_name = "id"
    _insert_format = "name, count, price"

    def __init__(self, path_to_db):
        self._path = path_to_db

    def connect(self):
        self.sqlite_connection = sqlite3.connect(self._path)
        self.sqlite_cursor = self.sqlite_connection.cursor()

    def add_row(self, table_name="", row_array=list()):
        self.sqlite_cursor.execute("INSERT INTO {} ({}) VALUES ({})"
                                   .format(table_name, self._insert_format,
                                           str(row_array)[1:-1]))

    def delete(self, table_name="", id_array=list()):
        self.sqlite_cursor.execute("DELETE FROM {} WHERE {} IN ({})"
                                   .format(table_name, self._id_column_name,
                                           str(id_array)[1:-1]))

    def decrease(self, id_array=list()):
        if not id_array:
            return
        self.adapter.decrease(id_array)

    def reserve(self, id_array=list()):
        if not id_array:
            return
        self.adapter.reserve(id_array)

    def update(self, id, row_array=list()):
        if not row_array or (id < 0):
            return
        self.adapter.update(id, row_array)

    def commit(self):
        self.sqlite_connection.commit()

    def select_all(self, table_name=""):
        yield from self.sqlite_cursor.execute("SELECT * FROM {}"
                                              .format(table_name))

    def close_connection(self):
        self.sqlite_connection.close()
