import os

def info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return None, None

path = input("Enter the path: ")

filename, directory = info(path)

if filename and directory:
    print("Filename:", filename)
    print("Directory:", directory)
else:
    print("The path does not exist.")
