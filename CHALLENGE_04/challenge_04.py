# In a world where information is power, a hacker known as Savipo Yatar discovers a series of files on a highly protected server.

# These files contain secrets that could change the course of history. But there's a problem: some of the files are fake, designed to deceive intruders. Savipo Yatar must quickly determine which files are real and which are fake.

# Each file has a name with two parts, separated by a hyphen (-). The first part is an alphanumeric string, and the second is a checksum, which is a string formed by the characters that only appear once in the first part and in the order in which they appear.

# Write a program that determines whether a file is real or fake based on these rules.

# Function to check the validity of a file based on its filename
def check_file(filename: str) -> bool:
  # Split the filename into name and checksum parts
  keys: list[str] = filename.split('-')
  name: str
  checksum: str
  name, checksum = keys
  appeared_once: list[str] = []

  for letter in checksum:
    if name.count(letter) == 1:
      appeared_once.append(letter)
    else:
      return False

  # Get the index of the letters that appeared only once in the name
  letters_index: list[int] = [name.index(letter) for letter in appeared_once]

  # Check if there is at least one letter that appeared only once, and if the indexes are in sequential order
  if len(appeared_once) >= 1 and sorted(letters_index) == letters_index:
    return True
  else:
    return False
  
with open('CHALLENGE_04/files.txt', 'r') as files:
  real_files: list[str] = [file.strip() for file in files if check_file(file.strip())]
  fake_files: list[str] = [file.strip() for file in files if not check_file(file.strip())]

print('Real Files:')
for i, file in enumerate(real_files, 1):
  print(f'{i}. {file}')

print('\nFake Files:')
for i, file in enumerate(fake_files, 1):
  print(f'{i}. {file}')