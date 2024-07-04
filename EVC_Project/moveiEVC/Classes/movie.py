from abc import ABC
from datetime import datetime
from typing import List, Dict, Any
from ticket_type import TicketType


class Movie(ABC):
    """
    This class represents a movie showing.
    """
    def __init__(self, id: int, name: str, description: str, poster_url: str,
                 show_date: datetime, show_time: str, ticket_types: List[TicketType]):
        self._id = id
        self._name = name
        self._description = description
        self._poster_url = poster_url
        self._show_date = show_date
        self._show_time = show_time
        self._ticket_types = ticket_types

    def get_category(self):
        pass

class ActionMovie(Movie):
    def get_category(self):
        return "Action"

class ComedyMovie(Movie):
    def get_category(self):
        return "Comedy"

class DramaMovie(Movie):
    def get_category(self):
        return "Drama"

class FantasyMovie(Movie):
    def get_category(self):
        return "Fantasy"
    
class HorrorMovie(Movie):
    def get_category(self):
        return "Horror"
    
class ScifiMovie(Movie):
    def get_category(self):
        return "Sci-fi"

# دالة لتحديد نوع الفيلم
def print_movie_category(movie: Movie):
    print(f"The category of this movie is: {movie.get_category()}")

    

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id: int):
        if not isinstance(new_id, int):
            raise TypeError("ID must be an integer")
        self._id = new_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")
        self._name = new_name


    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description: str):
        if not isinstance(new_description, str):
            raise TypeError("Description must be a string")
        self._description = new_description

    @property
    def poster_url(self):
        return self._poster_url

    @poster_url.setter
    def poster_url(self, new_poster_url: str):
        if not isinstance(new_poster_url, str):
            raise TypeError("Poster URL must be a string")
        self._poster_url = new_poster_url

    @property
    def show_date(self):
        return self._show_date

    @show_date.setter
    def show_date(self, new_show_date: datetime):
        if not isinstance(new_show_date, datetime):
            raise TypeError("Show date must be a datetime object")
        self._show_date = new_show_date

    @property
    def show_time(self):
        return self._show_time

    @show_time.setter
    def show_time(self, new_show_time: str):
        if not isinstance(new_show_time, str):
            raise TypeError("Show time must be a string")
        self._show_time = new_show_time

    @property
    def ticket_types(self):
        return self._ticket_types
