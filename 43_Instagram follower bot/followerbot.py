from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

SIMILAR_ACCOUNT = "arenabreakoutglobal" # Change this to an account of your choice
INSTA_EMAIL_ID = "YOUR_EMAIL_ID_USED_TO_LOGIN"
INSTA_PASSWORD = "YOUR_PASSWORD"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        login.send_keys(INSTA_EMAIL_ID)
        sleep(2)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password.send_keys(INSTA_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(10)
        not_now_cookie = self.driver.find_element(By.XPATH, "//div[contains(text(), 'Not now')]")
        not_now_cookie.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        sleep(5)
        ul = self.driver.find_elements(By.TAG_NAME, 'li')
        print(ul[1].text)
        ul[1].click()
        sleep(2)
        try:
            follow = [i for i in self.driver.find_elements(By.XPATH, "//button[@type='button']")]
            print(follow)
            for follower in follow[2:]:
                sleep(2)
                follower.click()
        except NoSuchElementException:
            pass
        except ElementClickInterceptedException:
            pass


bot = InstaFollower()
bot.login()
sleep(5)
bot.find_followers()
