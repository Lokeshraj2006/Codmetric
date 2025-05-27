# Movie Rating Analysis

This project estimates movie ratings from IMDb reviews based on their sentiment labels. Instead of using actual numeric ratings, sentiment (positive or negative) is used to classify reviews into approximate rating bands:

- **Positive sentiment → Estimated rating: 7–10**
- **Negative sentiment → Estimated rating: 1–4**

A bar chart visualizes the distribution of these estimated ratings.

## Key Insights

- The dataset reveals a **balanced distribution** of sentiments, indicating a near-equal number of reviews in both the 7–10 and 1–4 rating bands.
- This balance suggests the dataset is suitable for **training or evaluating sentiment analysis models**.

## Key Components Used

### Data Handling: `pandas`

- Loaded and manipulated the dataset.
- Created a new column:  
  `Rating_Estimate` based on sentiment labels.
- Used `value_counts()` to count reviews within each rating range.

### Logic & Transformation

- Utilized **lambda functions and conditional logic** to assign estimated ratings from sentiment labels.

### Visualization: `seaborn` & `matplotlib`

- Created a **bar chart** using `seaborn.barplot()` to show the number of reviews in each rating category.
- Enhanced layout and presentation with `tight_layout()`.

### Clean Plot Design

- Added **labels and titles** for clarity.
- Used a **coolwarm** color palette to visually distinguish between the rating categories.

---

This project demonstrates how textual sentiment can be translated into meaningful numeric estimations, enabling basic yet effective visual analysis of review data.
