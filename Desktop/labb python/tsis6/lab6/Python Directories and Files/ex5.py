def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"The list has been'{filename}'.")
    except IOError:
        print("Error:")

input_list = input("Enter the list elements: ").split(',')

input_list = [element.strip() for element in input_list]

filename = input("Enter the filename: ")

write_list_to_file(filename, input_list)
