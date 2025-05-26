import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# Load the IMDb dataset
df = pd.read_csv("C:\\Users\\LOKESHRAJ M\\IMDB Dataset.csv")

# --- Part 1: Rating Trends ---
# Estimate ratings based on sentiment
df['Rating_Estimate'] = df['sentiment'].apply(lambda x: '7-10' if x == 'positive' else '1-4')
rating_counts = df['Rating_Estimate'].value_counts().sort_index()

# Plot rating trend
plt.figure(figsize=(6, 4))
sns.barplot(x=rating_counts.index, y=rating_counts.values, palette="coolwarm")
plt.title("Estimated Rating Distribution from Sentiment")
plt.xlabel("Rating Range")
plt.ylabel("Number of Reviews")
plt.tight_layout()
plt.show()

# --- Part 2: Genre Popularity ---
# Define keyword-based genre categories
genre_keywords = {
    'action': ['fight', 'battle', 'war', 'explosion', 'guns'],
    'comedy': ['funny', 'laugh', 'humor', 'hilarious', 'joke'],
    'drama': ['emotional', 'relationship', 'life', 'realistic'],
    'romance': ['love', 'romantic', 'relationship'],
    'horror': ['scary', 'horror', 'ghost', 'killer', 'murder'],
    'thriller': ['thriller', 'suspense', 'mystery'],
    'sci-fi': ['space', 'alien', 'future', 'technology'],
    'fantasy': ['magic', 'dragon', 'fantasy', 'sword'],
    'animation': ['animated', 'cartoon', 'pixar', 'disney'],
    'documentary': ['documentary', 'true story', 'biography'],
    'crime': ['crime', 'detective', 'mafia', 'heist']
}

# Count genre mentions based on review text
genre_counts = {genre: 0 for genre in genre_keywords}
genre_counts['unknown'] = 0

for review in df['review']:
    review_lower = review.lower()
    matched = False
    for genre, keywords in genre_keywords.items():
        if any(re.search(rf"\b{kw}\b", review_lower) for kw in keywords):
            genre_counts[genre] += 1
            matched = True
    if not matched:
        genre_counts['unknown'] += 1

# Create DataFrame for genre counts
genre_df = pd.DataFrame(list(genre_counts.items()), columns=['Genre', 'Mentions']).sort_values(by='Mentions', ascending=False)

# Plot genre popularity
plt.figure(figsize=(10, 6))
sns.barplot(data=genre_df, x='Genre', y='Mentions', palette='coolwarm')
plt.title("Estimated Genre Popularity Based on Review Mentions")
plt.xlabel("Genre")
plt.ylabel("Number of Mentions in Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# the second graph would take time to run as it processes the entire dataset