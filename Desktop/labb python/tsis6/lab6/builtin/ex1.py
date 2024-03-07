def multiply(chislo):
    result = 1
    for num in chislo:
        result *= num
    return result

user = input("Enter numbers: ")
chislo = [int(num) for num in user.split()]

result = multiply(chislo)
print("Result:", result)
