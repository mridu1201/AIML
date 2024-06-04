from collections import Counter
import string
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def most_frequent_words(text):
 # Tokenize the text into words
 words = nltk.word_tokenize(text)

 # Remove punctuation marks
 words = [word.lower() for word in words if word.isalnum()]

 # Filter out stop words
 stop_words = set(stopwords.words('english'))
 words = [word for word in words if word not in stop_words]

 # Count occurrences of each word
 word_counts = Counter(words)

 # Get the 50 most frequent words
 top_50_words = word_counts.most_common(50)

 return top_50_words
# Example text
text = """Text and speech analysis in AI and Python programming for
experiment. Python is a powerful language used in AI and text
processing. Python's NLTK library provides tools for text analysis."""
# Call the function and print the results
result = most_frequent_words(text)
print("50 Most Frequent Words (excluding stop words):\n")
for word, count in result:
 print(f"{word}: {count}")
