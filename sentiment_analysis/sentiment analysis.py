#  Import necessary libraries
import pandas as pd
import string
import matplotlib.pyplot as plt
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load reviews from a text file (one review per line)
with open(r"C:\Users\LOKESHRAJ M\Intern\codmetric\sentiment_analysis\test.ft.txt", "r", encoding="utf-8") as file:
    reviews = file.readlines()

# Convert to DataFrame
df = pd.DataFrame(reviews, columns=["Review"])

# Text preprocessing function
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Apply preprocessing
df['Cleaned_Review'] = df['Review'].astype(str).apply(preprocess)

# Sentiment analysis
def get_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment'] = df['Cleaned_Review'].apply(get_sentiment)
# Visualization - Bar Chart
sentiment_counts = df['Sentiment'].value_counts()

# Bar Chart
sentiment_counts.plot(kind='bar', color=['green', 'gray', 'red'])
plt.title("Sentiment Distribution - Bar Chart")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Pie Chart
sentiment_counts.plot(kind='pie', autopct='%1.1f%%', colors=['green', 'gray', 'red'])
plt.title("Sentiment Distribution - Pie Chart")
plt.ylabel("")
plt.tight_layout()
plt.show()
