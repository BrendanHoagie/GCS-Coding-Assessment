"""
User model representing a user in a hypothetical database for this application
"""
from typing import Optional
from models.city import City

# constant
_MAX_NUM_FAVS = 3

class User:
    
    def __init__(self, favorites: Optional[list[City]] = None) -> None:
        """
        Initializes a User instance
        
        Args:
            favorites - optional List of City objects
        """
        if not favorites:
            self._favorites = []
        else:
            self._favorites = favorites[:_MAX_NUM_FAVS]
        
    def can_add_to_favorites(self) -> bool:
        """
        Determines whether a new city can be added to the favorites list
        
        Returns:
            True if favorites list is not full, otherwise False
        """
        return len(self._favorites) < _MAX_NUM_FAVS
    
    def add_to_favorites(self, c: City) -> None:
        """
        Adds a city to the favorites list.

        Args:
            city - City object to add
        """
        if isinstance(c, City):
            self._favorites.append(c)
        
    def display_favorites(self) -> None:
        """
        Displays weather details for all favorite cities
        """
        if self._favorites == []:
            print("No cities saved as favorites. Try adding one first!\n")
        for city in self._favorites:
            city.display()
        
    def get_favorite_city_names(self) -> list[str]:
        """
        Returns a list of favorite city names.
        """
        return [city.get_name() for city in self._favorites]
        
    def remove_from_favorites(self, index: int) -> None:
        """
        Removes a city from favorites by index.

        Args:
            index - position of the city in the favorites list
        """
        self._favorites.pop(index)
        
        
        
        