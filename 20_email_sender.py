import smtplib

MY_EMAIL = "___YOUR_EMAIL_HERE____"
MY_PASSWORD = "___YOUR_PASSWORD_HERE___"

"""We can write `connection = smtplib.SMTP("smtp.gmail.com", 587)` to initialise the connection nut then we will need 
to close the line using `connection.clode()`. Therefor as we did in the files case, we can use `with smtplib.SMTP(
host, port) as connection` to avoid extra line."""

with smtplib.SMTP("__YOUR_SMTP_ADDRESS_HERE___") as connection:
    """
    The string in the bracket shows that how we are going to connect to the Internet provider. 
    host = Gmail    -> smtp.gmail.com
           Hotmail  -> smtp.live.com
           Yahoo    -> smtp.mail.yahoo.com
    """
    connection.starttls()  # Secures the connection with our email server(ENCRYPTS THE MESSAGE)
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs="RECIEVER_EMAIL@myyahoo.com", msg="Subject:Hello\n\nThis is the body of "
                                                                                    "the email.")

