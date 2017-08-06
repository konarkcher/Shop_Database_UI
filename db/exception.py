class DbException(Exception):
    """Cutsom db exception, value infromation is stroed in self.message"""

    def __init__(self, message):
        super(DbException, self).__init__(message)
