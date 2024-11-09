from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>  Method using "X-path"  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
event = {}
for i in range(1, 6):
    event_date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/time')
    event_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[{i}]/a')
    event[i] = {"date": event_date.text,
                "name": event_name.text,
                "link": event_name.get_attribute("href")}

print(event)

# >>>>>>>>>>>>>>>>>>>>>>>>>> Alternate method using "find_elements" <<<<<<<<<<<<<<<<<<<<<<<<<<<<

tier_1 = driver.find_elements(By.CLASS_NAME, value="tier-1")
event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")  # The elements are iterable
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}
for n in range(len(event_dates)):
    events[n+1] = {
        "time": event_dates[n].text,
        "name": event_names[n].text,
        "link": event_names[n].get_attribute("href")
    }

print(events)

driver.quit()
