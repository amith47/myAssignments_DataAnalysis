import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('weather_data.db')

# Query to retrieve all weather data
query = "SELECT * FROM Weather"
df = pd.read_sql_query(query, conn)

# City-wise Data Analysis
print("City-wise Data Analysis:")
print(df[['city', 'temperature', 'humidity']])

# Filter cities with temperature above a certain threshold (e.g., 30°C)
hot_cities = df[df['temperature'] > 30]
print("\nCities with temperature above 30°C:")
print(hot_cities)

# Sort results by temperature
sorted_by_temp = df.sort_values(by='temperature', ascending=False)
print("\nSorted cities by temperature:")
print(sorted_by_temp[['city', 'temperature']])

# Group cities by weather conditions
grouped_conditions = df.groupby('weather_description').size()
print("\nCities grouped by weather conditions:")
print(grouped_conditions)

# Calculate average temperature and humidity
average_temp = df['temperature'].mean()
average_humidity = df['humidity'].mean()
print(f"\nAverage Temperature: {average_temp:.2f}°C")
print(f"Average Humidity: {average_humidity:.2f}%")

# Find highest and lowest temperatures
highest_temp = df['temperature'].max()
lowest_temp = df['temperature'].min()
print(f"\nHighest Temperature: {highest_temp:.2f}°C")
print(f"Lowest Temperature: {lowest_temp:.2f}°C")

# Close the database connection
conn.close()