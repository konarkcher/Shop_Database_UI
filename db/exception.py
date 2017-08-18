import enum


class ConstraintErrorType(enum.Enum):
    INCORRECT_VALUE = enum.auto()
    TOO_LONG = enum.auto()
    NOT_UNIQUE = enum.auto()

class DbErrorType(enum.Enum):
    UNDEFIEND_ERROR = enum.auto()
    ALREADY_EXISTS = enum.auto()
    NO_SUCH_TABLE = enum.auto()


class DbException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    def __init__(self, message, type_num=DbErrorType.UNDEFIEND_ERROR):
        super(DbException, self).__init__(message)
        self.message = message
        self.type_num = type_num

    def set_type(type_num):
        self.type_num = type_num


class ConstraintException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    def __init__(self, message, column_name, type_num):
        super(ConstraintException, self).__init__(message)
        self.column_name = column_name
        self.type_num = type_num


