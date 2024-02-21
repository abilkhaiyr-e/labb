#Write a Python program to subtract five days from current date


from datetime import datetime, timedelta


now = datetime.now()
five_days_ago = now - timedelta(days=5)


print("Current Date:", now.strftime("%Y-%m-%d"))
print("Five days ago:", five_days_ago.strftime("%Y-%m-%d"))
