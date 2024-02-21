#Write a Python program to print yesterday, today, tomorrow.

from datetime import datetime, timedelta

now = datetime.now()

yesterday = now - timedelta(days=1)
tomorrow = now + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", now.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))
