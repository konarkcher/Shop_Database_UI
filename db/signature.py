class Column:
    def __init__(self, name, display_name, prop, description):
        self.name = name  # for db and class of each string
        self.display_name = display_name  # link to locale
        self.proportion = prop  # for auto resize
        self.description = description  # approx type for db


class Table:
    def __init__(self, name):
        self.name = name
        self.columns = list()

    def add_column(self, column):
        self.columns.append(column)


class Database:
    def __init__(self, name):
        self.name = name
        self.tables = list()

    def add_table(self, table):
        self.tables.append(table)
