from .exception import DbException


class Manager:
    """Db managment class"""

    def __init__(self, adapter):
        self.adapter = adapter
        try:
            self.adapter.connect()
        except Exception as e:
            raise DbException(e.args[0])

    def __str__(self):
        return "This is DbManager with " + self.adapter

    def add_row(self, table_name="", row_sig="", row_array=list()):
        if not row_array or not table_name:
            return
        self.adapter.add_row(table_name,  row_sig, row_array)
        self.commit()

    def delete(self, table_name="", id_array=list()):
        if not id_array:
            return
        try:
            self.adapter.delete(table_name, id_array)
            self.commit()
        except Exception as e:
            raise DbException(e.args[0])

    def reserve(self, id_array=list()):
        if not id_array:
            return
        try:
            self.adapter.reserve(id_array)
            self.commit()
        except Exception as e:
            raise DbException(e.args[0])

    def decrease(self, id_array=list()):
        if not id_array:
            return
        try:
            self.adapter.decrease(id_array)
            self.commit()
        except Exception as e:
            raise DbException(e.args[0])

    def update(self, id, row_array=list()):
        if not row_array or (id < 0):
            return
        try:
            self.adapter.update(id, row_array)
            self.commit()
        except Exception as e:
            raise DbException(e.args[0])

    def commit(self):
        self.adapter.commit()

    def select_all(self, table_name=""):
        if not table_name:
            return
        try:
            yield from self.adapter.select_all(table_name)
        except Exception as e:
            raise DbException(e.args[0])

    def select_by_id(self, table_name="", id_array=list()):
        if not id_array:
            return []
        try:
            yield from self.adapter.select_by_id(table_name, id_array)
        except Exception as e:
            raise DbException(e.args[0])

    def close_connection(self):
        try:
            self.adapter.close_connection()
        except Exception as e:
            raise DbException(e.args[0])

    def create_tables(self):
        try:
            self.adapter.create_tables()
        except Exception as e:
            raise DbException(e.args[0])
