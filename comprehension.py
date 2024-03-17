# Store a list of words
words = ["apple", "banana", "orange", "kiwi", "pineapple", "Alvolyne", "Alfred", "Adhiambo", "Emali", "Kombo"]

# Use list comprehension to create a new list with words having odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)
