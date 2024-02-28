import re
x = str(input())
y = re.sub('(.)([A-Z][a-z]+)',r'\1_\2', x)
z = re.sub('([a-z0-9])([A-Z])', r'\1_\2', y).lower()
print(z)