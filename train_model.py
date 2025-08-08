import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset (replace with your own if needed)
data = pd.DataFrame({
    "text": [
        "The president signed a new bill today",
        "Scientists discover cure for common cold",
        "You won't believe what this celebrity did!",
        "Miracle weight loss pill revealed!",
        "NASA confirms Mars water evidence",
        "Click here to claim your lottery prize",
    ],
    "label": [1, 1, 0, 0, 1, 0]  # 1 = Real, 0 = Fake
})

X_train, X_test, y_train, y_test = train_test_split(data['text'], data['label'], test_size=0.2, random_state=42)

# Vectorize text
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved.")
