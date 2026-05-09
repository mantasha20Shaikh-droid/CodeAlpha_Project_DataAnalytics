# TASK 4 : SENTIMENT ANALYSIS
'''
TASK 4: Sentiment Analysis
- Classify reviews
- NLP processing
- Detect emotions
- Understand public opinion
- Create insights from text
'''
print("TASK 4 : SENTIMENT ANALYSIS")
# Import Libraries
from textblob import TextBlob
from wordcloud import WordCloud

# Dynamic Reviews Dataset
reviews = [
    "Absolutely fantastic product and amazing support!",
    "Worst experience ever, very disappointed.",
    "Delivery was fast and packaging was excellent.",
    "The product quality is average.",
    "I love this service, highly recommended!",
    "Not worth the money.",
    "Superb quality and beautiful design.",
    "Terrible customer support.",
    "It works perfectly for my needs.",
    "Mediocre experience overall."
]
# Sentiment Function
def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Analyze Reviews
sentiment_results = []
for review in reviews:
    sentiment = analyze_sentiment(review)
    polarity_score = TextBlob(review).sentiment.polarity
    sentiment_results.append({
        "Review": review,
        "Polarity": polarity_score,
        "Sentiment": sentiment
    })
# Create DataFrame
sentiment_df = pd.DataFrame(sentiment_results)
# Display Results
print("\n Sentiment Analysis Results:\n")
print(sentiment_df)

# Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x="Sentiment", data=sentiment_df)
plt.title("Sentiment Distribution")
plt.show()

# Generate WordCloud
all_text = " ".join(reviews)
wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white"
).generate(all_text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Customer Review WordCloud")
plt.show()
