import re
txt = str(input())
r = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(r)