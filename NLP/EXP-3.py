# Morphological Analysis using NLTK

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required resources (only first time)
nltk.download('wordnet')
nltk.download('omw-1.4')

# Create objects
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

print("\nOriginal Words:")
print(words)

print("\nStemming:")
for word in words:
    print(word, "->", stemmer.stem(word))

print("\nLemmatization:")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word))
