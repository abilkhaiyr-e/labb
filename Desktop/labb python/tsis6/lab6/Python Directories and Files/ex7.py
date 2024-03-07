def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except IOError:
        print("Error: Unable to copy contents.")

# Input the source and destination file names
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

# Copy the contents of the source file to the destination file
copy_file(source_file, destination_file)
