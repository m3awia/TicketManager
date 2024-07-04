from typing import List, Dict, Any

from movie import Movie
from ticket_type import TicketType
from movie_ticket import MovieTicket
from seat import Seat


class VIPTicket(MovieTicket):
    #subclass
    def __init__(self, movie: "Movie", seat: Seat, vip_benefits: List[str] = None):
        super().__init__(movie, TicketType.VIP)
        self.seat = seat
        self.ticket_type =TicketType.VIP

    def get_price(self):
        return 65.00

