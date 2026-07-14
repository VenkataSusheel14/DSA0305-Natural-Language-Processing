import re

# Input from user
text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

# Search for the pattern
match = re.search(pattern, text)

# Display result
if match:
    print("Pattern found!")
    print("Matched text:", match.group())
    print("Starting position:", match.start())
    print("Ending position:", match.end())
else:
    print("Pattern not found.")
