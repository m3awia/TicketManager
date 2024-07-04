class Seat:
    """
    This class represents a seat in a movie theater.
    """
    def __init__(self, row: int, number: int):
        self.row = row
        self.number = number

    def __str__(self):
        return f"Row: {self.row}, Number: {self.number}"
