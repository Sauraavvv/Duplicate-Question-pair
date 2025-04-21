import nltk
import pickle
from nltk.corpus import stopwords

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Save stopwords to pickle file
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(stop_words, f)

print("Stopwords pickle file created successfully!") 