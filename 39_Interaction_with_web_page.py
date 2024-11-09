from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")

first_name.send_keys("B. Rohan")
last_name.send_keys("Rao")
email.send_keys("Rohan@gmail.com", Keys.ENTER)  # This keys.enter functions as pressing enter button.


# submit = driver.find_element(By.CSS_SELECTOR, "form button")
# submit.click()  #This is another way which we can locate the button in the page and click it
