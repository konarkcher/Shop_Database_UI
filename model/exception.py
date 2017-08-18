import enum


class ValidationErrorType(enum.Enum):
    INCORRECT_VALUE = enum.auto()
    TOO_LONG = enum.auto()


class ValidationException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    def __init__(self, message, column_dict):
        super(ConstraintException, self).__init__(message)
        self.message = message
        self.column_dict = column_dict

    def get_dict(self):
    	return self.column_dict
