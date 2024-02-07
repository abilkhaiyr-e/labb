def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 3, 3, 4, 4, 5]
unique_list = unique_elements(original_list)
print("Original list:", original_list)
print("Unique elements:", unique_list)