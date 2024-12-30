
# THIS CODE IS NOT RUNNABLE

# It just shows us how we can change between different window in selenium.
# Point to be noted is the index i.e. '[0]' and '[1]' for 1st window and 2nd window

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)
sleep(8)

