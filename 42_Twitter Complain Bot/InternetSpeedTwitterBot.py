from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_USERNAME = "YOUR TWITTER USER"
TWITTER_EMAIL = "YOUR TWITTER EMAIL"
TWITTER_PASSWORD = "YOUR TWITTER PASSWORD"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        sleep(60)

        down_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div['
                                                        '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div['
                                                        '2]/span')
        up_speed = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div['
                                                      '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div['
                                                      '2]/span')

        print(up_speed.text)
        print(down_speed.text)
        return up_speed.text, down_speed.text

    def tweet_at_provider(self, up_speed, down_speed):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://twitter.com/login")
        sleep(5)
        email = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div['
                                                         '2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)
        try:
            sleep(6)
            user_id = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div['
                                                         '2]/div/input')

            user_id.send_keys(TWITTER_USERNAME)
            user_id.send_keys(Keys.ENTER)
        except NoSuchElementException:
            pass
        sleep(6)
        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                            '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                            '3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)
        sleep(6)
        tweet_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                       '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                       '1]/div/div/div/div[2]/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/div/div/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/div/span')

        tweet_box.send_keys(f"My internet speed is too slow, here is what I'm getting "
                            f"Download Speed: {down_speed}Mbps, Upload Speed: {up_speed}Mbps. Which isn't "
                            f"your guaranteed speed")

        tweet_box.send_keys(Keys.ENTER)

        post_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div['
                                                         '2]/main/div/div/div/div/div/div[3]/div/div[2]/div['
                                                         '1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        post_button.click()
        sleep(2)
        self.driver.quit()


speed = InternetSpeedTwitterBot()

up, down = speed.get_internet_speed()
print(up, down)
speed.tweet_at_provider(up, down)
