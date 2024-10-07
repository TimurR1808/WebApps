from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Kansas City"):

    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={f503358a208fb1c3d54d48ebbc1b5b93}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # Check for empty strings or string with only spaces
    # This step is not required here
    # if not bool(city.strip()):
    #     city = "Kansas City"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
