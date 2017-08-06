class DbManager:
    """Db managment class"""

    def __init__(self, adapter):
        self.adapter = adapter
        self.adapter.connect()

    def __str__(self):
        return "This is DbManager with " + self.adapter

    def add_row(self, table_name="", row_array=list()):
        if not row_array or not table_name:
            return
        self.adapter.add_row(table_name, row_array)
        self.commit()

    def delete(self, table_name="", id_array=list()):
        if not id_array:
            return
        self.adapter.delete(table_name, id_array)

    def reserve(self, id_array=list()):
        if not id_array:
            return
        self.adapter.reserve(id_array)

    def decrease(self, id_array=list()):
        if not id_array:
            return
        self.adapter.decrease(id_array)

    def update(self, id, row_array=list()):
        if not row_array or (id < 0):
            return
        self.adapter.update(id, row_array)

    def commit(self):
        self.adapter.commit()

    def select_all(self, table_name=""):
        if not table_name:
            return
        yield from self.adapter.select_all(table_name)

    def close_connection(self):
        self.adapter.close_connection()
