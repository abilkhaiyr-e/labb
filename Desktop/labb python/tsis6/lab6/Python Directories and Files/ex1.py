import os

def directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    return directories

def files(path):
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return files

def all(path):
    all_contents = [content for content in os.listdir(path)]
    return all_contents

path = input("Enter the path: ")

print("Directories:")
print(directories(path))

print("\nFiles:")
print(files(path))

print("\nAll Directories and Files:")
print(all(path))
