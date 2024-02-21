def generator(n):
    while n >= 0:
        yield n
        n -= 1


n = int(input("Number: "))

for output in generator(n):
    print(output)