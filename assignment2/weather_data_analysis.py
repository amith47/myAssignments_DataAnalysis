import requests
import matplotlib.pyplot as plt
import seaborn as sns

#  OpenWeatherMap API key
API_KEY = 'd9125b152daf4cec4302f2399bc0750e'

# List of Indian cities and Karnataka districts to fetch weather data for
cities = [
    "Bangalore",  # Karnataka
    "Mysore",  # Karnataka
    "Hubli",  # Karnataka
    "Mangalore",  # Karnataka
    "Gulbarga",  # Karnataka
    "Belgaum",  # Karnataka
    "Dharwad",  # Karnataka
    "Delhi",  # India
    "Mumbai",  # India
    "Kolkata",  # India
    "Chennai",  # India
    "Hyderabad"  # India
]

# Base URL for the OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather"


# Function to fetch weather data for a given city
def fetch_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()


# Collecting weather data
weather_data = []

for city in cities:
    data = fetch_weather(city)
    if data.get('cod') == 200:  # Check if the request was successful
        city_weather = {
            'City': data['name'],
            'Temperature (°C)': data['main']['temp'],
            'Humidity (%)': data['main']['humidity'],
            'Weather Description': data['weather'][0]['description'],
            'Wind Speed (m/s)': data['wind']['speed']
        }
        weather_data.append(city_weather)
    else:
        print(f"Failed to get data for {city}: {data.get('message')}")

# Analyzing humidity levels
if weather_data:
    # Extract humidity data
    humidity_data = {entry['City']: entry['Humidity (%)'] for entry in weather_data}

    # Find the city with the highest humidity
    highest_humidity_city = max(humidity_data, key=humidity_data.get)
    highest_humidity = humidity_data[highest_humidity_city]

    # Find the city with the lowest humidity
    lowest_humidity_city = min(humidity_data, key=humidity_data.get)
    lowest_humidity = humidity_data[lowest_humidity_city]

    print(f"\nCity with the highest humidity: {highest_humidity_city} ({highest_humidity} %)")
    print(f"City with the lowest humidity: {lowest_humidity_city} ({lowest_humidity} %)")

    # Check for patterns between temperature and humidity
    temp_humidity_data = {entry['City']: (entry['Temperature (°C)'], entry['Humidity (%)']) for entry in weather_data}

    # Visualizations
    # 1. Compare temperatures across cities
    plt.figure(figsize=(10, 5))
    sns.barplot(x=[entry['City'] for entry in weather_data], y=[entry['Humidity (%)'] for entry in weather_data])
    plt.title("Humidity Levels Across Cities")
    plt.xticks(rotation=45)
    plt.ylabel("Humidity (%)")
    plt.show()

    # 2. Relationship between temperature and humidity
    temp_values = [entry['Temperature (°C)'] for entry in weather_data]
    humidity_values = [entry['Humidity (%)'] for entry in weather_data]

    plt.figure(figsize=(10, 5))
    sns.scatterplot(x=temp_values, y=humidity_values, hue=[entry['City'] for entry in weather_data], palette='viridis')
    plt.title("Temperature vs Humidity")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Humidity (%)")
    plt.show()

    # 3. Distribution of different weather conditions
    weather_conditions = {}
    for entry in weather_data:
        condition = entry['Weather Description']
        if condition not in weather_conditions:
            weather_conditions[condition] = 0
        weather_conditions[condition] += 1

    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(weather_conditions.keys()), y=list(weather_conditions.values()))
    plt.title("Distribution of Weather Conditions")
    plt.xticks(rotation=45)
    plt.ylabel("Number of Cities")
    plt.show()