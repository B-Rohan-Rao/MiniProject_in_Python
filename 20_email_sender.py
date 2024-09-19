import smtplib

my_email = "bb2304176@gmail.com"
password = "qomf hbya fpnp rzvt"

"""We can write `connection = smtplib.SMTP("smtp.gmail.com", 587)` to initialise the connection nut then we will need 
to close the line using `connection.clode()`. Therefor as we did in the files case, we can use `with smtplib.SMTP(
host, port) as connection` to avoid extra line."""

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    """
    The string in the bracket shows that how we are going to connect to the Internet provider. 
    host = Gmail    -> smtp.gmail.com
           Hotmail  -> smtp.live.com
           Yahoo    -> smtp.mail.yahoo.com
    """
    connection.starttls()  # Secures the connection with our email server(ENCRYPTS THE MESSAGE)
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="bumblebee33@myyahoo.com", msg="Subject:Hello\n\nThis is the body of "
                                                                                    "the email.")

