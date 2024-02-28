import re
txt = str(input())
r = '.*a(b{2,3})'
x = re.search(r, txt)
print(x.string)
