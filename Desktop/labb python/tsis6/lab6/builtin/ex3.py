def palindrome(s):
    return s == s[::-1]


user = input("Enter: ")

if palindrome(user):
    print("Yes")
else:
    print("No")
