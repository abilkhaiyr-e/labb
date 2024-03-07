import os

def delete_file(path):
    try:
        # Check if the path exists
        if not os.path.exists(path):
            print("Error: The specified path does not exist.")
            return

        # Check for access permissions
        if not os.access(path, os.R_OK | os.W_OK):
            print("Error: You don't have sufficient permissions to delete the file.")
            return

        # Delete the file
        os.remove(path)
        print(f"The file '{path}' has been successfully deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input the file path from the user
file_path = input("Enter the path of the file to delete: ")

# Delete the file
delete_file(file_path)
