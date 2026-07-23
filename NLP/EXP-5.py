# Import Porter Stemmer
from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# Input words from user
words = input("Enter words separated by spaces: ").split()

print("\nStemmed Words:")
for word in words:
    print(word, "->", ps.stem(word))
