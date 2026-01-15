"""
The City class is a wrapper around the data returned by the API
"""
class City:
    
    def __init__(self, data: dict) -> None:
        """
        Initalizes a City object from API response data
        
        Args:
            data - a dictionary returned by the OpenWeather API
        """
        self._city = data["name"]
        self._country = data["sys"]["country"]
        self._temperature = data["main"]["temp"]
        self._feels_like = data["main"]["feels_like"]
        self._humidity = data["main"]["humidity"]
        self._weather_desc = data["weather"][0]["description"].title()
        self._wind_speed = data["wind"]["speed"]
        
    def get_name(self) -> str:
        """
        Returns the name of the City
        """
        return self._city
    
    def display(self) -> None:
        """
        Prints the formatted weather details for the City
        """
        print("\nWeather Details")
        print("-" * 30)
        print(f"City: {self._city}, {self._country}")
        print(f"Temperature: {self._temperature}°C")
        print(f"Feels Like: {self._feels_like}°C")
        print(f"Condition: {self._weather_desc}")
        print(f"Humidity: {self._humidity}%")
        print(f"Wind Speed: {self._wind_speed} m/s\n")