#Write a Python program to drop microseconds from datetime.

from datetime import datetime


now = datetime.now()


without_microseconds = now.replace(microsecond=0)


print("Original:", now)
print("Without microseconds:", without_microseconds)
