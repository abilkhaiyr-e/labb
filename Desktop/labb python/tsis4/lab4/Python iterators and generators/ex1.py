def generator(n):
    for i in range(1,n+1):
        yield i**2

n=int(input("Number:"))

for output in generator(n):
    print(output)