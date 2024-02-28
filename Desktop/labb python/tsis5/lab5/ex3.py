import re
txt = str(input())
r = '^[a-z]+(_[a-z]+)*'
x = re.search(r, txt)
print(x)