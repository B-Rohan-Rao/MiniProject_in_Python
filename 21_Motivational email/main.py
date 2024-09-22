import datetime as dt
import smtplib
import random

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
if day == 0:
    try:
        with open("quotes.txt") as data:
            quotes = data.readlines()
        with smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="RECIEVER_EMAIL@gmail.com", msg=random.choice(quotes))

    except FileNotFoundError:
        print("The file quotes.txt was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"Its {weekdays[day]}")
