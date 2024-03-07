import string

def create_text_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("This is file " + filename)

create_text_files()
