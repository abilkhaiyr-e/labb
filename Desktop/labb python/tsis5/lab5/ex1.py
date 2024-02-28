import re
txt = str(input())
r = "^a(b*)$"
x = re.search(r, txt)
print(x)