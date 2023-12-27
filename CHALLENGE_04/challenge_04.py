# In a world where information is power, a hacker known as Savipo Yatar discovers a series of files on a highly protected server.

# These files contain secrets that could change the course of history. But there's a problem: some of the files are fake, designed to deceive intruders. Savipo Yatar must quickly determine which files are real and which are fake.

# Each file has a name with two parts, separated by a hyphen (-). The first part is an alphanumeric string, and the second is a checksum, which is a string formed by the characters that only appear once in the first part and in the order in which they appear.

# Write a program that determines whether a file is real or fake based on these rules.

def check_file(filename):
  filename = filename.split("-")
  name = filename[0]
  checksum = filename[1]
  appeared_once = []

  for letter in checksum:
    if name.count(letter) == 1:
      appeared_once.append(letter)
    else:
      return False

  letters_index = [name.index(letter) for letter in appeared_once]

  if len(appeared_once) >= 1 and sorted(letters_index) == letters_index:
    return True
  else:
    return False
  
real_files = []
fake_files = []

with open("CHALLENGE_04/files.txt", "r") as files:
  for file in files:
    if check_file(file.strip()):
        real_files.append(file.strip())
    else:
        fake_files.append(file.strip())

print("Archivos reales:")
for i, file in enumerate(real_files, 1):
    print(f"{i}. {file}")

print("\nArchivos falsos:")
for i, file in enumerate(fake_files, 1):
    print(f"{i}. {file}")