import enum

class DbException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    UNDEFIEND_ERROR = enum.auto()
    ALREADY_EXISTS = enum.auto()
    NO_SUCH_TABLE = enum.auto()

    def __init__(self, message, typeNum=UNDEFIEND_ERROR):
        super(DbException, self).__init__(message)
        self.message = message
        self.typeNum = typeNum


class ConstraintException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    INCORRECT_VALUE = enum.auto()
    TOO_LONG = enum.auto()
    NOT_UNIQUE = enum.auto()

    def __init__(self, message, column_name, typeNum):
        super(ConstraintException, self).__init__(message)
        self.column_name = column_name
        self.typeNum = typeNum
