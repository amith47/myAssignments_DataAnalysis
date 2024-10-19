import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
conn = sqlite3.connect('weather_data.db')

# Query to retrieve weather data
df = pd.read_sql_query("SELECT * FROM Weather", conn)

# Visualization of temperature distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['temperature'], bins=10, kde=True)
plt.title('Temperature Distribution Across Cities')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')
plt.show()

# Visualization of humidity distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['humidity'], bins=10, kde=True)
plt.title('Humidity Distribution Across Cities')
plt.xlabel('Humidity (%)')
plt.ylabel('Frequency')
plt.show()

# Close the database connection
conn.close()