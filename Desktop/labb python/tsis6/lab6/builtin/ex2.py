def count_string(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())

    return upper_count, lower_count



user = input("Enter string: ")


upper_count, lower_count = count_string(user)


print("upper count:", upper_count)
print("lower count:", lower_count)
