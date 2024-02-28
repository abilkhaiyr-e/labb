import re 
txt = str(input())
r = '^[A-Z][a-z]+$'
x = re.search(r, txt)
print(x)