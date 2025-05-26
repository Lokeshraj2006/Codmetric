# Titanic Survival Analysis

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("C:\\Users\\LOKESHRAJ M\\Downloads\\titanic\\train.csv") 

# Step 1: Handle Missing Values 
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df = df.drop(columns=['Cabin']) 

# Step 2: Encode Categorical Variables
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Create Age Group bins
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 20, 40, 60, 80], labels=['Child', 'Teen', 'Adult', 'Middle Age', 'Senior'])

# Step 3: Visualize Survival Rates
plt.figure(figsize=(15, 10))

# 1. Survival by Gender
plt.subplot(2, 2, 1)
sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate by Gender')
plt.xticks([0, 1], ['Male', 'Female'])

# 2. Survival by Passenger Class
plt.subplot(2, 2, 2)
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Survival Rate by Class')

# 3. Survival by Age Group
plt.subplot(2, 2, 3)
sns.barplot(x='AgeGroup', y='Survived', data=df)
plt.title('Survival Rate by Age Group')

# 4. Survival by Embarked_S
plt.subplot(2, 2, 4)
sns.barplot(x='Embarked_S', y='Survived', data=df)
plt.title('Survival Rate: Embarked S (1 = Yes)')

plt.tight_layout()
plt.show()


# MIT License
# Copyright (c) 2025 Lokeshraj M
# See LICENSE file for details.
