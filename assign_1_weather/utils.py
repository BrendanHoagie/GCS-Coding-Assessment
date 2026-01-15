"""
Utility functions, constants, and global state

If I had more time, this would be where I would set up a database rather than storing everything in memory.
It would be nice to have my data saved between instances.This would come with some changes.
For example, USER would be a user ID number for a database. Instead of using them directly, I would have
database lookup functions that would return state to operate on

Additionally, I would not store my api key file in this public git repository. Ideally, this would 
be stored locally, not in the project files. I could set it as an environment variable, then
read that locally. This is very bad security as I've currently set it up, but for a toy example that
must be completely put onto a public github page, I've done my best to obscure my API key.
"""

import sys
from models.user import User

# constant
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

# global state
API_KEY = None
USER = None


def tool_startup() -> None:
    """
    Initalizes global application state.
    Loads OpenWeather API key from file and creates a User instance
    
    Exits the program if API key cannot be loaded
    """
    global API_KEY
    global USER
    
    try:
        with open('api_key', 'r') as file:
            API_KEY = file.read()
    except FileNotFoundError:
        sys.exit("Error, OpenWeather API key could not be found. Exiting")
    except Exception as e:
        sys.exit(f"An unexpected error occurred: {e}. Exiting")
    
    USER = User()
    

def take_cli_input_with_options(options: dict[str, callable]) -> callable:
    """Displays a list of otions then handles CLI input.
    Uses a standard system where options are stored in a dictionary

    Args:
        options - a dictionary where each key-value pair is a string and a function

    Returns:
        the chosen function from the options list
    """
    
    option_names = list(options.keys())
    while True:
        for i, name in enumerate(option_names, start=1):
            print(f"{i}. {name}")

        try:
            choice = int(input(f"Enter a number 1-{len(option_names)}: "))
            if not 1 <= choice <= len(option_names):
                raise ValueError("Choice out of range")

            selected_name = option_names[choice - 1]
            return options[selected_name]

        except ValueError as e:
            print("Unrecognized input, please try again")
    
