# Finally, hackers have managed to access the database and have corrupted it. But it seems they have left a hidden message in the database. Can you find it?

# Our database is in .csv format. The columns are id,username,email,age,location.

# A user is only valid if:

# - id: exists and is alphanumeric
# - username: exists and is alphanumeric
# - email: exists and is valid (follows the pattern user@domain.com)
# - age: is optional but if it appears it is a number
# - location: is optional but if it appears it is a text string

import re

# Function to validate users based on the previous parameters
def validate_user(id: str, username: str, email: str, age: str = '0', location: str = '') -> bool:
  # Regular expression for validating email format
  regex: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

  if id.isalnum() and (username.isalnum() or username.isalpha()) and re.fullmatch(regex, email) and age.isnumeric():
    return True
  
  return False
  
invalid_users: list[str] = []

with open('CHALLENGE_05/data.csv', 'r') as data:
  for user in data:
    # Split the user information into fields using comma as a delimiter
    fields: list[str] = user.strip().split(',')

    if not validate_user(*fields):
      invalid_users.append(user.strip())

for i, user in enumerate(invalid_users, 1):
  print(f'{i}. {user}')

# Create a hidden message using the first letter of each invalid user's name
message: str = ''.join([user.split(',')[1][0] for user in invalid_users])

print(f'\nHidden message: {message}')