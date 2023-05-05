import collections

# Define the collection of documents as a list of strings
documents = [
    "The quick brown fox jumps over the lazy level",
    "Lorem ipsum dolor sit amet, anna consectetur adipiscing elit",
    "Sed do eiusmod tempor incididunt ut labore et dolore magna racecar aliqua",
    "Ut enim ad minim veniam, quis nostrud level exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"
]

all_text = " ".join(documents)

words = all_text.split()

palindrome_words = [word for word in words if word == word[::-1]]

palindrome_counts = collections.Counter(palindrome_words)

for word, count in palindrome_counts.items():
    print(word, count)
