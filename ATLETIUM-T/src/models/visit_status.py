from enum import Enum


class VisitStatus(Enum):
    none = 1
    present = 2
    absent = 3
    ill = 4
