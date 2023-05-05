import collections

documents = [
    "The quick brown fox jumps over the lazy dog",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"
]

all_text = " ".join(documents)

words = all_text.split()

word_counts = collections.Counter(words)

for word, count in word_counts.items():
    print(word, count)
