# A spy is sending encrypted messages.

# Your mission is to create a program that decodes the messages.

# The messages are words separated by spaces like this:
# cat dog dog car Cat doG sun

# We need the program to return the number of times each word appears in the message, regardless of whether it is in uppercase or lowercase.

# The result will be a text string with the word and the number of times it appears in the message, in this format:
# cat2dog3car1sun1

# The words are sorted by their first appearance in the message!

message = input("Write the message: ").lower()
words = message.split()
ordered_words = []

for word in words:
  if word not in ordered_words:
    ordered_words.append(word)

# Count the occurrences of each unique word in the original message
total_words = [str(message.count(word)) for word in ordered_words]
result = ""

# Iterate through the unique words and their corresponding counts
for i in range(len(ordered_words)):
  result = result + ordered_words[i] + total_words[i]

print(f"\n{result}")