def all_true_in_tuple(t):
    return all(t)

# User input for the tuple
user_input = input("Enter elements of the tuple separated by spaces: ")
user_tuple = tuple(map(bool, user_input.split()))

# Check if all elements in the tuple are True and print the result
print(all_true_in_tuple(user_tuple))
