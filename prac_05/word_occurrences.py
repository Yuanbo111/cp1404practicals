"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""

text = input("Text: ").lower()
words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Get the length of the longest word for formatting
max_length = max(len(word) for word in word_counts)

# Sort the words alphabetically and print with formatting
for word in sorted(word_counts):
    print(f"{word:{max_length}} : {word_counts[word]}")


