def generator(a,b):
    for i in range(a,b+1):
        yield i**2

a=int(input("Number1:"))
b=int(input("Number2:"))

for output in generator(a,b):
    print(output)