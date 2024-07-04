from typing import List, Dict, Any

from movie import*
from ticket_type import TicketType
from movie_ticket import MovieTicket
from seat import Seat

class StandardTicket(MovieTicket):
    """
    This sub class represents a standard movie ticket.
    """
    def __init__(self, movie: "Movie", seat: Seat):
        super().__init__(movie, TicketType.STANDARD)  # Pass TicketType.STANDARD explicitly
        self.seat = seat
        self.ticket_type = TicketType.STANDARD  # Store ticket_type as an attribute

    def get_price(self):
        if self.ticket_type == TicketType.STANDARD:
            return 45.00  # Or consider setting a base price in MovieTicket
        else:
            raise ValueError("Unexpected ticket type for StandardTicket")

    def __str__(self):
        return super().__str__() + f", Seat: {self.seat}"
