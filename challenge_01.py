# A spy is sending encrypted messages.

# Your mission is to create a program that decodes the messages.

# The messages are words separated by spaces like this:
# cat dog dog car Cat doG sun

# We need the program to return the number of times each word appears in the message, regardless of whether it is in uppercase or lowercase.

# The result will be a text string with the word and the number of times it appears in the message, in this format:
# cat2dog3car1sun1

# The words are sorted by their first appearance in the message!

message: str = input('Write the message: ').lower()
words: list[str] = message.split()
ordered_words: list[str] = []

for word in words:
  if word not in ordered_words:
    ordered_words.append(word)

# Count the occurrences of each unique word in the original message
total_words: list[str] = [str(message.count(word)) for word in ordered_words]

# Iterate through the unique words and their corresponding counts
result: str = ''.join([word + i for word, i in zip(ordered_words, total_words)])

print(f'\n{result}')
