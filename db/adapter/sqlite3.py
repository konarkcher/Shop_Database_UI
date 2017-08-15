import sqlite3

class Sqlite3:
    """
    docstring for sqlite3Adapter

    now this class is signature influenced in cause of add_row(...) function.

    """

    def __init__(self, path_to_db):
        self._path = path_to_db
        self._id_column_name = "id"
        self._reserved_column_name = "reserved"

    def connect(self):
        self.sqlite_connection = sqlite3.connect(self._path)
        self.sqlite_cursor = self.sqlite_connection.cursor()

    def add_row(self, table_name="", row_sig="", row_array=list()):
        self.sqlite_cursor.execute("INSERT INTO {} ({}) VALUES ({})"
                                   .format(table_name,
                                           row_sig,
                                           ("?, "*len(row_array))[:-2]
                                           ),
                                   tuple(row_array)
                                   )
        self.sqlite_connection.commit()
        return self.sqlite_cursor.lastrowid

    def delete(self, table_name="", id_array=list()):
        self.sqlite_cursor.execute("DELETE FROM {} WHERE {} IN ({})"
                                   .format(table_name,
                                           self._id_column_name,
                                           str(id_array)[1:-1]))

    def decrease(self, table_name="", column_name="", id_array=list()):
        self.sqlite_cursor.execute(
            "UPDATE {} SET {} = {} - 1 WHERE {} in ({})".format(
                table_name,
                column_name,
                self._id_column_name,
                str(id_array)[1:-1]
            ))

    def reserve(self, table_name="", pair_array=list()):
        for pair in pair_array:
            self.sqlite_cursor.execute(
                "UPDATE {} SET {} = {} + {} WHERE {} = {}".format(
                    table_name,
                    self._reserved_column_name,
                    self._reserved_column_name,
                    pair[1],
                    self._id_column_name,
                    pair[0]
                ))
        self.sqlite_connection.commit()

    def unreserve(self, table_name="", pair_array=list()):
        for pair in pair_array:
            self.sqlite_cursor.execute(
                "UPDATE {} SET {} = {} - {} WHERE {} = {}".format(
                    table_name,
                    self._reserved_column_name,
                    self._reserved_column_name,
                    pair[1],
                    self._id_column_name,
                    pair[0]
                ))
        self.sqlite_connection.commit()

    def update(self, table_name, column_name, id, value):
        print("UPDATE {} SET {} = ? WHERE {} = {}".format(
                table_name,
                column_name,
                self._id_column_name,
                id
            ))
        print(value)
        self.sqlite_cursor.execute(
            "UPDATE {} SET {} = ? WHERE {} = {}".format(
                table_name,
                column_name,
                self._id_column_name,
                id
            ), tuple([value]))
        self.sqlite_connection.commit()

    def commit(self):
        self.sqlite_connection.commit()

    def select_all(self, table_name=""):
        yield from self.sqlite_cursor.execute("SELECT * FROM {}"
                                              .format(table_name))

    def select_by_id(self, table_name="", id_array=list()):
        yield from self.sqlite_cursor.execute(
            "SELECT * FROM {} WHERE {} IN ({})"
            .format(
                table_name,
                self._id_column_name,
                str(id_array)[1:-1]))

    def close_connection(self):
        self.sqlite_connection.close()

    def create_tables(self):
        qry = open('db/adapter/scripts/sqlite/create.sql', 'r').read()
        self.sqlite_cursor.executescript(qry)
        self.sqlite_connection.commit()

    def execute(self, exec_str):
        self.sqlite_cursor.execute(exec_str)
