import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('gpa.csv')
df = pd.DataFrame(data)

# Data Analysis
print("Data Overview:")
print(df.describe())

# Data Visualization
plt.figure(figsize=(12, 6))

# Scatter plot of Study Week vs. GPA, color-coded by Gender
plt.scatter(df['studyweek'], df['gpa'], c=df['gender'].map({'female': 'blue', 'male': 'red'}), label=df['gender'], alpha=0.7)
plt.xlabel('Study Week')
plt.ylabel('GPA')
plt.title('Scatter Plot of Study Week vs. GPA')
plt.legend()
plt.grid(True)
plt.show()

# Box plot of Sleep Night, grouped by Gender
plt.figure(figsize=(8, 6))
df.boxplot(column='sleepnight', by='gender')
plt.title('Box Plot of Sleep Night by Gender')
plt.xlabel('Gender')
plt.ylabel('Sleep Night')
plt.suptitle("")  # Removing the default title
plt.show()

# Histogram of Out
plt.figure(figsize=(8, 6))
plt.hist(df['out'], bins=5, edgecolor='k', alpha=0.7)
plt.xlabel('Out')
plt.ylabel('Frequency')
plt.title('Histogram of Out')
plt.grid(True)
plt.show()
