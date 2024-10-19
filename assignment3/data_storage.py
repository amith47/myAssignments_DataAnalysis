import requests
import sqlite3

# OpenWeatherMap API key
API_KEY = 'd9125b152daf4cec4302f2399bc0750e'

# List of cities to fetch weather data for
cities = [
    "Bangalore", "Mysore", "Delhi", "Mumbai", "Kolkata", "Chennai", "Hyderabad"
]

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather"

# Connect to SQLite database (or create it)
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Create a table to store weather data
cursor.execute('''
CREATE TABLE IF NOT EXISTS Weather (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT,
    temperature REAL,
    humidity REAL,
    weather_description TEXT
)
''')


# Function to fetch weather data and store it in the database
def fetch_and_store_weather_data():
    for city in cities:
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get('cod') == 200:  # Check if the request was successful
            city_weather = (
                data['name'],
                data['main']['temp'],
                data['main']['humidity'],
                data['weather'][0]['description']
            )
            cursor.execute('''
            INSERT INTO Weather (city, temperature, humidity, weather_description)
            VALUES (?, ?, ?, ?)
            ''', city_weather)
            conn.commit()
        else:
            print(f"Failed to get data for {city}: {data.get('message')}")


# Fetch and store the weather data
fetch_and_store_weather_data()

# Close the database connection
conn.close()