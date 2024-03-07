def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return None

filename = input("Enter the text file name: ")

lines = count_lines(filename)
if lines is not None:
    print(f"Number of lines in the file '{filename}': {lines}")
