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


for word in sorted(word_counts):
        print(f"{word:} : {word_counts[word]}")


