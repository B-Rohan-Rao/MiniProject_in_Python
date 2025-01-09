from selenium import webdriver

# keeping the website open after the program is executed
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")


# driver1.close()  # Closes the tab as soon as it gets loaded
driver.quit()  # Shut down the entire browser.

