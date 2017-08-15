import enum

class DbException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    def __init__(self, message):
        super(DbException, self).__init__(message)
        self.message = message


class ConstraintException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    TOO_LONG = enum.auto()
	INCORRECT_TYPE = enum.auto()
	NOT_UNIQUE = enum.auto()

    def __init__(self, message, column_name):
        super(DbException, self).__init__(message)
        self.column_name = column_name
