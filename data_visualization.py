import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the data from the CSV file
data = pd.read_csv('OSHack_BankCustomers.csv')

# Data exploration and visualization

# Example 1: Basic bar chart
# Let's assume you want to visualize the distribution of ages
age_counts = data['age'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(age_counts.index, age_counts.values)
plt.xlabel('age')
plt.ylabel('balance')
plt.title('Distribution of Ages')
plt.show()

# Example 2: Scatter plot
# Visualizing the relationship between Age and Balance
plt.figure(figsize=(10, 6))
plt.scatter(data['age'], data['balance'], alpha=0.5)
plt.xlabel('age')
plt.ylabel('balance')
plt.title('Scatter Plot of Age vs. Balance')
plt.show()

# Example 3: Histogram
# Visualizing the distribution of balance
plt.figure(figsize=(10, 6))
plt.hist(data['balance'], bins=20, edgecolor='k')
plt.xlabel('balance')
plt.ylabel('duration')
plt.title('Histogram of Balance')
plt.show()

# Example 4: Pie chart
# Visualizing the distribution of Gender
marital_counts = data['marital'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(marital_counts, labels=marital_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('marital Distribution')
plt.show()

# You can add more visualizations based on your specific dataset and requirements.

# Save figures to a file
# plt.savefig('example_plot.png')

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['age'], data['balance'], data['duration'], c='b', marker='o')
ax.set_xlabel('age')
ax.set_ylabel('balance')
ax.set_zlabel('duration')
plt.title('3D Scatter Plot')
plt.show()