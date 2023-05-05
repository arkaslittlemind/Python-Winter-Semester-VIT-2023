import collections

documents = [
    "The quick brown fox jumps over the lazy dog",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat"
]

all_text = " ".join(documents)

words = all_text.split()

word_groups = collections.defaultdict(list)
for word in words:
    word_groups[len(word)].append(word)

group_counts = collections.Counter(len(word) for word in words)

for length, count in group_counts.items():
    print(f"Words with {length} letters:")
    for word in word_groups[length]:
        print(f"   {word}")
    print(f"Total count: {count}")
