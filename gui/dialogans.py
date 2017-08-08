import enum


class DlgAnswer(enum.Enum):
    NOT_CHOSEN = enum.auto()
    SQLITE_OPEN = enum.auto()
    SQLITE_CREATE = enum.auto()
