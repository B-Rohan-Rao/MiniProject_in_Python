import datetime as dt
import pandas as pd
from random import randint
import smtplib

MY_EMAIL = "bb2304176@gmail.com"
PASSWORD = "qomf hbya fpnp rzvt"

today = (dt.datetime.now().month, dt.datetime.now().day)

data = pd.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in new_dict:
    birthday_person = new_dict[today]
    file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:HAPPY BIRTHDAY\n\n{contents}")


