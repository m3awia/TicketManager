from abc import ABC, abstractmethod
from enum import Enum
from typing import List, Dict, Any

from movie import Movie


class MovieTicket(ABC):
    """
    This abstract class represents a general movie ticket. It defines common attributes and methods for different types of tickets.
    Subclasses like StandardTicket and VIPTicket should implement the abstract 'get_price' method.
    """

    def __init__(self, movie: "Movie", ticket_type: Enum):
        self.movie = movie
        self.ticket_type = ticket_type

    @abstractmethod
    def get_price(self):
        raise NotImplementedError("Subclasses must implement get_price")

    def __str__(self):
        return f"Ticket Type: {self.ticket_type}" + f"Movie: {self.movie.name}, At {self.movie.show_time}"