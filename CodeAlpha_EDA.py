# TASK 2 : EXPLORATORY DATA ANALYSIS (EDA)

'''
TASK 2: Exploratory Data Analysis
- Ask meaningful questions
- Understand data structure
- Find trends & anomalies
- Statistical testing
- Detect missing values
'''

print("TASK 2 : EXPLORATORY DATA ANALYSIS")

# Import Libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = sns.load_dataset("titanic")

# Basic Information
print("\n Dataset Preview:\n")
print(df.head())

print("\n Dataset Information:\n")
print(df.info())

print("\n Missing Values:\n")
print(df.isnull().sum())

print("\n Statistical Summary:\n")
print(df.describe())

# Meaningful Questions
print("\n EDA Questions:")
print("1. Which gender survived more?")
print("2. Does ticket class affect survival?")
print("3. Which age group had better survival?")
print("4. Are wealthy passengers safer?")

# Survival by Gender
gender_survival = df.groupby("sex")["survived"].mean()

print("\n Survival Rate by Gender:\n")
print(gender_survival)

# Survival by Passenger Class
class_survival = df.groupby("pclass")["survived"].mean()

print("\n Survival Rate by Class:\n")
print(class_survival)

# Detect Outliers
Q1 = df["fare"].quantile(0.25)
Q3 = df["fare"].quantile(0.75)

IQR = Q3 - Q1

outliers = df[(df["fare"] < (Q1 - 1.5 * IQR)) |
              (df["fare"] > (Q3 + 1.5 * IQR))]
print("\n Number of Fare Outliers :", len(outliers))
