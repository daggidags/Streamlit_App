import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer 
from sklearn.naive_bayes import MultinomialNB 
import joblib

df = pd.read_csv('C:/Users/angel/OneDrive/Desktop/DU/Advanced Topics/IMDB Dataset.csv')

X = df['review']
y = df['sentiment']

#print(df.head())

# Create a pipeline that first transforms the text data using TfidfVectorizer and then feeds it to the MultinomialNB classifier.
# Train the pipeline on your entire dataset (X and y). No need to create a train-test split for this assignment

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('nb', MultinomialNB())
])

pipeline.fit(X, y)

joblib.dump(pipeline, r'C:/Users/angel/OneDrive/Desktop/DU/Advanced Topics/sentiment_model.pkl')
print("✅ Model trained and saved as 'sentiment_model.pkl'")




