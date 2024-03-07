import os

def check_path_access(path):
    access_info = {
        'exists': os.path.exists(path),
        'readable': os.access(path, os.R_OK),
        'writable': os.access(path, os.W_OK),
        'executable': os.access(path, os.X_OK)
    }
    return access_info

# User input for the path
path = input("Enter the path: ")

# Check access to the specified path
access_info = check_path_access(path)

# Print the access information
print("Path exists:", access_info['exists'])
print("Readable:", access_info['readable'])
print("Writable:", access_info['writable'])
print("Executable:", access_info['executable'])
