"""
Command line interface logic for user interaction
"""

import requests
import utils
from models.user import User
from models.city import City

def cli() -> None:
    """
    Main CLI loop, displays available options and executes selected actions
    
    Throws KeyboardInterrupt on exit
    """
    options = {
        "Search for weather by city" : search_weather,
        "Add a city to your favorites" : add_city_to_favorites,
        "Display favorite city details" : display_favorites,
        "Update favorite cities": update_favorites,
        "Exit": cli_quit
    }
    
    while True:
        utils.take_cli_input_with_options(options)()
        
def search_weather(return_city : bool = False) -> City | None:
    """
    Prompts the user for a ciy name and retrieves weather data
    
    Args:
        return_city - if True, returns City object instead of displaying it
        
    Returns:
        City object if return_city is set, otherwise None
    """
        params = {
            "appid" : utils.API_KEY,
            "units" : "metric"
        }
        if not return_city:
            print("\n|-- Search for weather by city --|")
            print("-" * 34)
        while True:
            name = input("Enter the name of a city: ").strip()
            if not name:
                print("City name cannot be empty, try again")
            else:
                params["q"] = name
                break
        
        try:
            response = requests.get(utils.BASE_URL, params)
            response.raise_for_status()
            cur_city = City(response.json())
            if return_city:
                return cur_city
            else:
                cur_city.display()
        except requests.exceptions.RequestException as e:
            print(f"API could not process response. Please try again later.\n")
    

def add_city_to_favorites() -> None:
    """
    Add a city to the global user's favorite list if space allows
    """
    print("\n|-- Add a city to your favorites --|")
    print("-" * 36)
    if utils.USER.can_add_to_favorites():
        new_city = search_weather(return_city = True)
        utils.USER.add_to_favorites(new_city)
    else:
        print(f"Error: You are at the maximum number of favorites. Please delete one from the list before you try to add another.")
        
def display_favorites() -> None:
    """
    Displays weather details for all cities in the global user's favorite list
    """
    print("\n|-- Favorite City Details --|")
    print("-" * 29)
    utils.USER.display_favorites()
    
def update_favorites() -> None:
    """
    Allows the user to remove and add cities in their favorite list
    """
    print("\n|-- Update Favorite City List --|")
    print("-" * 29)
    city_names = utils.USER.get_favorite_city_names()

    if len(city_names) == 0:
        print("No cities in favorite list to edit. Try adding one first\n")
        return
        
    print("Pick one of the following cities to edit:")
    selected_city_index = 0

    while True:
        for i, city in enumerate(city_names, start=1):
            print(f" {i}. {city}")
            
        try:
            choice = int(input(f"Enter a number 1-{len(city_names)}: "))
            if not 1 <= choice <= len(city_names):
                raise ValueError("Choice out of range")

            selected_city_index = choice - 1
            break

        except ValueError as e:
            print("Unrecognized input, please try again")
    
    choice = input(f"Would you like to delete {city_names[selected_city_index]} from your Favorites? Type y for yes, anything else for no: ")
    if choice.lower() == 'y':
        print(f"Removing")
        utils.USER.remove_from_favorites(selected_city_index)
    choice = input(f"Would you like to add a new city to your favorites? Type y for yes, anything else for no: ")
    if choice.lower() == 'y':
        add_city_to_favorites()

def cli_quit() -> None:
    """
    Raises an error to notify the main program to exit the CLI loop gracefully
    """
    raise KeyboardInterrupt