class Column:
    def __init__(self, name, display_name, prop, description):
        self.name = name  # for db and class of each string
        self.display_name = display_name  # link to locale
        self.proportion = prop  # for auto resize
        self.description = description  # approx type for db


class Base:
    def __init__(self, name):
        self.name = name
        self.columns = list()

    def append(self, column):
        self.columns.append(column)
