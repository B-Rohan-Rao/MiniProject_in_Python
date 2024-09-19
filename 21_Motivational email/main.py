import datetime as dt
import smtplib
import random

my_email = "bb2304176@gmail.com"
password = "qomf hbya fpnp rzvt"
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = dt.datetime.now()
year = now.year
month = now.month
day = now.weekday()
if day == 0:
    try:
        with open("quotes.txt") as data:
            quotes = data.readlines()
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="bumblebee33@myyahoo.com", msg=random.choice(quotes))

    except FileNotFoundError:
        print("The file quotes.txt was not found.")

    except Exception as e:
        print(f"An error occurred: {e}")

else:
    print(f"Its {weekdays[day]}")
