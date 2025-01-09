from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib

# Configure Chrome options to keep the browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Define email credentials for SMTP authentication
my_email = "YOUR-EMAIL"
password = "YOUR-PASSOWORD"

# Define the URL of the product on Amazon
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Initialize the WebDriver with specified options and open the URL
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Extract the dollar and cents parts of the product price
price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction").text

# Retrieve the product title
product_title = driver.find_element(By.ID, "productTitle").text

# Display the product title and full price in the console for verification
print(product_title)
available_price = float(f"{price_dollar}.{price_cents}")
print(available_price)

# Close the browser tab (driver1.quit() would close the entire browser session)
driver.quit()

# Define the price threshold for sending an alert
my_price = 100.0

# ====================== Send the email if the product is below the target price ===========================


if available_price < my_price:
    # Compose the email message with the product details
    message = f"{product_title} is on sale. Price: ${available_price}\n(MESSAGE FROM SELENIUM)"

    # Set up an SMTP connection to Gmail's server to send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Start TLS encryption for secure email transmission
        connection.login(user=my_email, password=password)  # Log in with email credentials
        # Send the email with subject and body, encoded in UTF-8 to avoid encoding issues
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bumblebee33@myyahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
