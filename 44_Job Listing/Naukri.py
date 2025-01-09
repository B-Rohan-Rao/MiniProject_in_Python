from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

USER_ID = "Your Email id"
USER_PASSWORD = "Your passowrd"


class Naukri:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.driver1 = webdriver.Chrome(options=chrome_options)
        self.driver2 = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver1, 20)

    def login(self):
        self.driver1.get("https://www.naukri.com")
        sleep(1)
        login_button = self.driver1.find_element(By.XPATH, '//*[@id="login_Layer"]')
        login_button.click()
        sleep(1)

        username = self.driver1.find_element(By.XPATH,
                                             '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input')
        username.send_keys(USER_ID)
        password = self.driver1.find_element(By.XPATH,
                                             '//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[3]/input')
        password.send_keys(USER_PASSWORD)
        password.send_keys(Keys.ENTER)

    def job_search(self, job_role, job_location, job_scrapper_pages):
        try:
            sleep(1.5)
            parts = job_role.split(" ")

            for i in range(job_scrapper_pages + 1):
                self.driver1.get(f"https://www.naukri.com/{parts[0]}-{parts[1]}-jobs-in-{job_location}-{i}")
                heading_xpath = '(//*[@class="srp-jobtuple-wrapper"])/div/div/a'
                link_xpath = '(//*[@class="srp-jobtuple-wrapper"])/div/div/a'
                subheading_xpath = '(//*[@class="srp-jobtuple-wrapper"])/div/div[2]//a'
                experience_xpath = '(//*[@class="srp-jobtuple-wrapper"])/div/div[3]/div/span[1]/span/span'
                salary_xpath = '(//*[@class="srp-jobtuple-wrapper"])/div/div[3]/div/span[2]/span/span'

                # Wait for elements to load
                heading_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, heading_xpath)))
                link_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, link_xpath)))
                subheading_elements = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, subheading_xpath)))

                headings = [element.text for element in heading_elements]
                links = [element.get_attribute('href') for element in link_elements]
                subheading = [element.text for element in subheading_elements]

                for j in range(len(headings)):
                    self.driver2.get(
                        "https://docs.google.com/forms/d/e/1FAIpQLScRR73FFOyShBwMhpbbvq_ZGoL4IYKR4v4okDM4krmKSSamoQ/viewform?usp=header"
                    )
                    sleep(2)

                    job_title = self.driver2.find_element(By.XPATH,
                                                          '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                    job_title.send_keys(headings[j])

                    job_link = self.driver2.find_element(By.XPATH,
                                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                    job_link.send_keys(links[j])

                    job_subheading = self.driver2.find_element(By.XPATH,
                                                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
                    job_subheading.send_keys(subheading[j])

                    submit_button = self.driver2.find_element(By.XPATH,
                                                              '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
                    submit_button.click()

        except Exception as e:
            print(f"An error occurred during job search: {e}")
        finally:
            try:
                if self.driver2:
                    self.driver2.quit()
                if self.driver1:
                    self.driver1.quit()
            except Exception as quit_error:
                print(f"An error occurred while quitting browsers: {quit_error}")


option = input(
    "What role do you want?\n 1. Python Developer\n 2. Data Analyst\n 3. Data Scientist\n 4. Web Developer\n").strip()

if option == "1":
    role = "Python Developer"
elif option == "2":
    role = "Data Analyst"
elif option == "3":
    role = "Data Scientist"
elif option == "4":
    role = "Web Developer"
else:
    print("Please select a valid option.")
    exit()  # Exit if an invalid option is chosen

# Taking other inputs
location = input("Enter your location:-\n").strip()
try:
    pages = int(input("How many pages do you want to scrape?\n").strip())
except ValueError:
    print("Please enter a valid number for pages.")
    exit()

job_searcher = Naukri()
job_searcher.login()
sleep(2)
job_searcher.job_search(role, location, pages)
