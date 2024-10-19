import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the employee dataset
file_path = 'Employee_data.xlsx'
employee_data = pd.ExcelFile(file_path)

# Check the sheet names to understand the structure of the file
sheet_names = employee_data.sheet_names
print(sheet_names)

# Load a specific sheet into a DataFrame (assuming you want the first sheet)
employee_data = employee_data.parse(sheet_names[0])
print(employee_data.head())

# Get information about data types and missing values
print(employee_data.info())

# Summary statistics for numerical columns
summary_stats = employee_data[['sales', 'salary', 'experience', 'age']].agg(['mean', 'median', 'max', 'min'])
print(summary_stats)

# Detecting outliers using Interquartile Range (IQR) for salary and sales
Q1 = employee_data[['sales', 'salary']].quantile(0.25)
Q3 = employee_data[['sales', 'salary']].quantile(0.75)
IQR = Q3 - Q1

# Filtering outliers
outliers = employee_data[
    (employee_data['sales'] < (Q1['sales'] - 1.5 * IQR['sales'])) |
    (employee_data['sales'] > (Q3['sales'] + 1.5 * IQR['sales'])) |
    (employee_data['salary'] < (Q1['salary'] - 1.5 * IQR['salary'])) |
    (employee_data['salary'] > (Q3['salary'] + 1.5 * IQR['salary']))
]

print(outliers)

# Average salary and total sales by department and region
dept_region_group = employee_data.groupby(['department', 'region']).agg(avg_salary=('salary', 'mean'), total_sales=('sales', 'sum')).reset_index()
print(dept_region_group)

# Top 5 employees with the highest sales
top_5_sales = employee_data.nlargest(5, 'sales')[['employee_name', 'sales']]
print(top_5_sales)

# Top 5 employees with the highest salaries
top_5_salaries = employee_data.nlargest(5, 'salary')[['employee_name', 'salary']]
print(top_5_salaries)

# Correlation between experience and salary
exp_salary_corr = employee_data['experience'].corr(employee_data['salary'])

# Correlation between experience and sales
exp_sales_corr = employee_data['experience'].corr(employee_data['sales'])

print(f"Correlation between experience and salary: {exp_salary_corr}")
print(f"Correlation between experience and sales: {exp_sales_corr}")

# Bar chart for sales distribution by department
plt.figure(figsize=(10, 6))
sns.barplot(x='department', y='sales', data=employee_data, errorbar=None)
plt.title('Sales Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()

# Scatter plot for experience vs salary
plt.figure(figsize=(10, 6))
sns.scatterplot(x='experience', y='salary', data=employee_data)
plt.title('Experience vs Salary')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.tight_layout()
plt.show()

# Bar chart for average salary by region
plt.figure(figsize=(10, 6))
sns.barplot(x='region', y='salary', data=employee_data, errorbar=None, estimator='mean')
plt.title('Average Salary by Region')
plt.xlabel('Region')
plt.ylabel('Average Salary')
plt.xticks(rotation=45)
plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels
plt.show()