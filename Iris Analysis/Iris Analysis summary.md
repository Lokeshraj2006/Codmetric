# Iris Dataset - Exploratory Data Analysis (EDA)

This project performs exploratory data analysis (EDA) on the famous Iris dataset to understand the structure, distribution, and relationships among features and species.

## Modules Used

- **pandas**: For data handling
- **numpy**: For numerical operations
- **matplotlib.pyplot & seaborn**: For creating visualizations
- **sklearn.datasets**: To load the Iris dataset

## Key Functions & Techniques

- `load_iris()` – Load the dataset from `sklearn.datasets`
- `DataFrame()` – Convert dataset into a structured table
- `head()`, `info()`, `describe()` – Explore data structure and summary statistics
- `isnull().sum()` – Check for missing values
- `corr()` – Compute correlation between features
- `heatmap()`, `pairplot()` – Generate visual insights

## Visualizations & Insights

### Heatmap (Correlation Matrix)

- Shows feature-to-feature relationships
- **Petal length and petal width** are strongly correlated
- **Sepal width** has a low correlation with other features

### Pairplot

- Plots each feature against every other
- **Setosa** is clearly separated from other species
- **Versicolor and Virginica** show some overlap

### Histogram / Distribution Plots

- Show spread and distribution of feature values
- **Petal features** show better separation by species than sepal features

### Boxplot

- Visualizes spread, median, and potential outliers
- Highlights which features vary significantly between species

## Data Insights

- **150 samples** with **4 features** and **3 species**
- No missing values in the dataset
- **Petal length and width** are more informative for classification
- **Setosa** is the easiest to classify based on its distinct feature patterns

## Conclusion

- The dataset is clean and suitable for machine learning modeling
- Visualizations effectively highlight feature relationships and species differences
- Ideal for learning and implementing classification algorithms like **KNN**, **SVM**, and others
