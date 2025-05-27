# Sentiment Analysis – Summary Report

**Author:** Lokeshraj M  
**License:** [MIT License](LICENSE)

---

##  Objective

The purpose of this task was to analyze product review texts to identify overall **sentiment** — _positive_, _neutral_, or _negative_ — and derive meaningful insights into customer perception and satisfaction.

---

##  Methodology

###  Data Source

- Dataset: `test.ft.txt` (plain text format)  
- Each line in the file represents a single product review.
- the dataset file was too large to upload so I was not able to upload it.

###  Preprocessing Steps

- Converted all text to **lowercase**
- Removed **punctuation** using the `string` module
- Removed **stopwords** using NLTK's English stopword list
- Applied **custom cleaning functions** for optimized preprocessing

###  Sentiment Analysis

- Performed using **TextBlob**  
- Sentiment polarity thresholds:
  - `Polarity > 0` → **Positive**
  - `Polarity = 0` → **Neutral**
  - `Polarity < 0` → **Negative**

---

##  Visualization

- A **pie chart** was created using **Matplotlib** to show the distribution of sentiment categories among reviews.

---

## Results

| Sentiment | Percentage |
|-----------|------------|
| Positive  | 75.3%      |
| Negative  | 22.6%      |
| Neutral   | 2.1%       |

---

## Insights

- **Majority positive (75.3%)** – Indicates high overall customer satisfaction.
- **Significant negative portion (22.6%)** – Highlights areas that may need attention or improvement.
- **Minor neutral feedback (2.1%)** – Few users left objective or undecided reviews.

---

## Conclusion

The sentiment distribution shows that **most customers are highly satisfied**, but there remains a **notable amount of dissatisfaction**. These insights can help:

- Improve product quality
- Enhance customer support
- Guide future business strategies

---

##  Tools & Libraries Used

- **Python**
- **TextBlob** – Sentiment polarity analysis
- **NLTK** – Text preprocessing and stopword removal
- **Matplotlib** – Visualization (Pie Chart)

---


