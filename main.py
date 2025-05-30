import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='whitegrid')
plt.style.use('seaborn-v0_8-muted')

# Load Dataset 
df = pd.read_csv(r"D:\\PythonPr\\netflix_titles.csv")

# Head of dataset
print("First 5 Rows:")
print(df.head())

# Basic info
print("Info:")
print(df.info())

# Summary stats
print("Description of numerical columns:")
print(df.describe())

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Fill missing values (No inplace to avoid FutureWarnings)
df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Unknown")
df['country'] = df['country'].fillna("Unknown")
df['rating'] = df['rating'].fillna("Unknown")
df['duration'] = df['duration'].fillna("Unknown")

# Convert 'date_added' to datetime (flexible format)
df['date_added'] = pd.to_datetime(df['date_added'], format='mixed', errors='coerce')
df['year_added'] = df['date_added'].dt.year

# Extract numeric duration and its type
df['duration_int'] = df['duration'].str.extract(r'(\d+)').astype(float)
df['duration_type'] = df['duration'].str.extract(r'([a-zA-Z]+)')

plt.figure(figsize=(6,4))
sns.countplot(data=df, x='type')
plt.title("Count of Movies and TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,6))
df['country'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title("Top 10 Countries with Most Netflix Titles")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12,6))
df['year_added'].value_counts().sort_index().plot(kind='bar', color='coral')
plt.title("Content Added to Netflix per Year")
plt.ylabel("Number of Titles Added")
plt.xlabel("Year Added")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,5))
sns.countplot(data=df, y='rating', order=df['rating'].value_counts().index)
plt.title("Distribution of Content Ratings")
plt.xlabel("Count")
plt.ylabel("Rating")
plt.show()

plt.figure(figsize=(10,6))
sns.histplot(df[df['type'] == 'Movie']['duration_int'], bins=30, color='orchid')
plt.title("Distribution of Movie Durations (in minutes)")
plt.xlabel("Duration (minutes)")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(data=df[df['type'] == 'TV Show'], x='duration_int')
plt.title("Number of Seasons in TV Shows")
plt.xlabel("Seasons")
plt.ylabel("Count")
plt.show()
