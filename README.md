ASSIGNMENT 1 :
Data Analytics Assignment: Employee Data Analysis and Visualization
Objective:
Analyze the Employee_data.xlsx file using Python (Pandas) and provide insights
through data manipulation and visualization. The goal is to understand key trends and
patterns in the employee data, focusing on departments, sales, salaries, and
experience. After completing the analysis, upload your final Python code and results
(visualizations) to your GitHub repository and share the public link.
Problem Statement:
You are tasked with analyzing the employee dataset to provide insights into company
performance and employee metrics. Your analysis should address the following key
questions:
Analysis Tasks:
o Provide basic summary statistics (mean, median, max, min) for key
numerical fields such as sales, salary, experience, and age.
o Identify any trends or outliers in the data.
2.
o Compare the average salary and total sales across different
departments and regions. Identify which department and region perform
the best in terms of these metrics.
o Which department has the highest average salary? Which department
generates the most sales?
3.
o Identify the top 5 employees with the highest sales and the top 5
employees with the highest salaries.
o Are the highest earners also the top performers in terms of sales?
4.
o Analyze the relationship between an employee's experience and their
salary. Does more experience consistently lead to higher pay?
o Investigate the correlation between experience and sales performance.
Does more experience lead to better sales figures?
5.
o Create at least 3 visualizations (e.g., bar charts, line graphs, scatter plots)
to represent:
▪ The distribution of sales across departments.
▪ The relationship between experience and salary.
▪ The comparison of average salaries across regions or departments.
Deliverables:
1. A detailed report summarizing your findings and insights for each analysis task.
2. 3 visualizations clearly showing key relationships and trends.
3. A Python script containing your full analysis and code.
4. Upload the Python code and visualizations to your GitHub repository and share
the public link.
Submission Instructions:
1. Complete the analysis using Python and necessary libraries (Pandas, Matplotlib,
Seaborn).
2. Ensure your code is clean, well-commented, and your visualizations are clear
and labeled.
3. Publish your Python notebook/script and visualizations to your GitHub
repository.
4. Submit the public GitHub link to your repository with your final code and
results.
------------------------------------------------------------------------------------------------------------------------------

ASSIGNMENT 2:
Data Analytics Assignment: Weather Data Analysis Using OpenWeatherMap API
Objective:
In this assignment, you will retrieve weather data using the OpenWeatherMap API
(https://openweathermap.org/api) and analyze it to gain insights into temperature,
humidity, and weather patterns across different cities. You will use Python to fetch the
data and perform analysis, followed by creating visualizations for better
understanding. Finally, you will upload your code and results to your GitHub repository
and share the public link.
Problem Statement:
You are tasked with retrieving current weather data for a list of cities using the
OpenWeatherMap API. Based on the retrieved data, perform analysis to identify key
patterns and trends in weather conditions (temperature, humidity, etc.) across different
cities.
Analysis Tasks:
o Register on https://openweathermap.org/api and get your API key.
o Write a Python script that:
▪ Sends requests to the OpenWeatherMap API to fetch weather
data for at least 10 cities of your choice.
▪ Collects data such as city name, temperature, humidity, weather
description, and wind speed.
2. Weather Data Analysis:
o Temperature Comparison:
▪ Compare the current temperatures across the selected cities.
▪ Identify the city with the highest and lowest temperature.
o Humidity Analysis:
▪ Analyze the humidity levels and find which cities have the highest
and lowest humidity.
▪ Is there a pattern between temperature and humidity across cities?
o Weather Conditions:
▪ Group the cities by general weather conditions (e.g., clear, cloudy,
rainy, etc.) and determine how many cities fall into each category.
3. Visualization:
o Create at least 3 visualizations (e.g., bar charts, scatter plots) that:
▪ Compare temperatures across cities.
▪ Show the relationship between temperature and humidity.
▪ Display the distribution of different weather conditions across the
cities.
4. Optional Advanced Analysis:
o Time-Based Analysis:
▪ If you want to expand the project, retrieve weather data over a
period of time (e.g., over several days) for one or more cities, and
analyze how temperature and humidity change over time.
o Weather Forecast:
▪ Retrieve forecast data using the 5-day forecast endpoint and
analyze trends for a single city.
Deliverables:
1. Python Script:
o A well-documented Python script that retrieves data from the
OpenWeatherMap API and performs the analysis.
2. Summary Report:
o A concise report summarizing key findings, such as the hottest and
coldest cities, humidity patterns, and any general weather trends.
3. Visualizations:
o At least 3 visualizations that provide insights into the weather data
across cities.
4. GitHub Upload:
o Upload your code and visualizations to your GitHub repository.
o Submit the public GitHub link to your repository.
Submission Instructions:
1. Register and get the API key from OpenWeatherMap.
2. Fetch the weather data using Python and analyze it according to the problem
statement.
3. Create the required visualizations and summarize your insights.
4. Publish your Python script, report, and visualizations to your GitHub repository.
------------------------------------------------------------------------------------------------------------------------------

ASSIGNMENT 3
Data Analytics Assignment: Storing and Analyzing Data with SQLite Using Python
Objective:
In this assignment, you will interact with an SQLite database using Python. You will
retrieve weather data (or another dataset) using an API, store the data in an SQLite
database, and then perform analysis by querying the database. The final output will
include both the Python code and the results of your analysis, uploaded to your GitHub
repository.
Problem Statement:
You are tasked with fetching data from the https://openweathermap.org/api (or
another API/dataset of your choice), storing the data in an SQLite database, and then
performing analysis by querying the database.
Analysis Tasks:
1. Data Retrieval and Storage:
o Choose a dataset to retrieve, such as weather data from the
OpenWeatherMap API, or any other public dataset/API of your choice.
o Use Python to:
▪ Send requests to the API and fetch the required data (e.g., weather
data for multiple cities).
▪ Create an SQLite database using sqlite3.
▪ Store the fetched data in the SQLite database in a well-structured
table format (e.g., with columns for city, temperature, humidity,
weather description, etc.).
o Ensure you can insert, update, and delete records in your SQLite database
as necessary.
2. Database Querying and Analysis:
o Write Python scripts to interact with your SQLite database and retrieve
data for analysis.
o Perform the following tasks by querying the database:
▪ City-wise Data Analysis:
▪ Retrieve and compare the current temperatures and
humidity levels for the cities stored in the database.
▪ Filter and Sort:
▪ Query the database to retrieve cities where the temperature
is above a certain threshold, or where humidity is lower
than a given value.
▪ Sort the results by temperature, humidity, or another
attribute.
▪ Group and Aggregate Data:
▪ Group cities by weather conditions (e.g., clear, cloudy, rainy)
and count how many cities fall into each category.
▪ Statistical Insights:
▪ Calculate the average temperature and humidity across all
cities in the database.
▪ Find the highest and lowest temperatures stored in the
database.
3. Visualization (Optional):
o Create visualizations based on the data retrieved from the SQLite
database:
▪ Visualize the distribution of temperature and humidity across
different cities.
▪ Show how many cities fall under different weather conditions.
o Use Matplotlib or Seaborn to generate these visualizations.
Deliverables:
1. Python Script for Data Storage:
o A Python script that retrieves the data from the API, stores it in an SQLite
database, and ensures the data is stored in a structured way (create
tables, insert records, etc.).
2. Database Queries and Analysis:
o Python scripts that query the SQLite database to perform the analysis
tasks mentioned above.
o Present the results of your analysis (e.g., which city has the highest
temperature, average humidity levels across all cities, etc.).
3. SQLite Database File:
o Save the SQLite database (.db file) and include it in your GitHub
repository.
4. Optional Visualizations:
o If you choose to visualize the data, include the visualizations in your
repository, either as images or as part of a Jupyter notebook.
5. GitHub Upload:
o Upload your Python scripts, SQLite database, and optional
visualizations to your GitHub repository.
o Submit the public GitHub link to your repository.
Submission Instructions:
1. Retrieve data using an API (e.g., OpenWeatherMap) or another dataset.
2. Store the data in an SQLite database using Python.
3. Write Python scripts to query the database and perform the analysis.
4. (Optional) Create visualizations based on your analysis.
5. Publish your code, database file, and visualizations to your GitHub repository.
6. Submit the public GitHub link to your final submission.
