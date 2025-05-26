# Import required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
iris = pd.read_csv("C:\\Users\\LOKESHRAJ M\\codmetric\\iris.csv")
print("First 5 rows of the dataset:")
print(iris.head())

# Summary statistics
print("\nSummary statistics:")
print(iris.describe())

# Histograms for feature distribution
iris.drop(columns=["species"]).hist(figsize=(10, 6), color='skyblue', edgecolor='black')
plt.suptitle("Histograms of Iris Features", fontsize=14)
plt.show()

#  Box plots for each feature
plt.figure(figsize=(10, 6))
sns.boxplot(data=iris.drop(columns=["species"]))
plt.title("Boxplot of Iris Features", fontsize=14)
plt.show()

# Pair plot to visualize feature relationships by species
sns.pairplot(iris, hue='species', height=2.5)
plt.suptitle("Pairplot of Iris Dataset", y=1.02)
plt.show()

# Correlation heatmap (only numeric columns)
iris_numeric = iris.drop(columns=["species"])
plt.figure(figsize=(8, 5))
sns.heatmap(iris_numeric.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Numeric Features", fontsize=14)
plt.show()
