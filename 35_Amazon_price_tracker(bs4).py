from bs4 import BeautifulSoup
import requests
import smtplib

# Define email and password for SMTP authentication
my_email = "YOUR-EMAIL"
password = "YOUR-PASSOWORD"

# URL for the product page on Amazon
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Define headers to mimic a real browser visit and avoid bot detection by Amazon
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 "
                  "Safari/537.36 OPR/114.0.0.0",
}

# or you can add minimal header
# header = {
#      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0"
#                   "Safari/537.36 OPR/114.0.0.0"
#     "Accept-Language": "en-US,en;q=0.9"
# }

# Send an HTTP GET request to fetch the webpage content
response = requests.get(url=URL, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

# Extract the product price by locating elements with specific classes for the price whole and fraction parts
price = soup.find(class_="a-price-whole").getText()
decimal = soup.find(class_="a-price-fraction").getText()

# Construct the full price as a float by combining the integer and decimal parts
available_price = float(f"{price}{decimal}")
print(available_price)

# Extract the product title by locating the element with the 'productTitle' ID
title = soup.find(id="productTitle").getText().strip()
print(title)

# Set the target price threshold for sending an alert
my_price = 100.0

# ====================== Send the email if the product is below the target price ===========================

if available_price < my_price:
    # Prepare the alert message with the product title, current price, and URL
    message = f"{title} is on sale. Price: ${available_price}\n(MESSAGE FROM BEAUTIFULSOUP)"

    # Establish an SMTP connection to Gmail's server
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Initiates a secure connection to the server
        connection.login(user=my_email, password=password)  # Log in to the email account
        # Send the email with a subject line and message body
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bumblebee33@myyahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
