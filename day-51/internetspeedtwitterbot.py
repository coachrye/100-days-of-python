import time
from selenium import webdriver

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/coachrye/SeleniumWebDriverProjects/chromedriver"
TWITTER_EMAIL = "rye@coachrye.com"
TWITTER_PASSWORD = "twitter!34"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.selenium = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.selenium.get("https://www.speedtest.net/")
        time.sleep(1)
        go_button = self.selenium.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        time.sleep(60)
        # self.selenium.implicitly_wait(180)
        download = self.selenium.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        upload = self.selenium.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        print(download.text)
        print(upload.text)

    def tweet_at_provider(self):
        self.selenium.get("https://twitter.com/login")
        time.sleep(3)
        username = self.selenium.find_element_by_name('session[username_or_email]')
        username.send_keys(TWITTER_EMAIL)
        password = self.selenium.find_element_by_name('session[password]')
        password.send_keys(TWITTER_PASSWORD)
        login = self.selenium.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        login.click()
        time.sleep(3)

        tweet = self.selenium.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        # my_message = f"Day "
        tweet.send_keys("testing")
        send_tweet = self.selenium.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        send_tweet.click()

        time.sleep(2)
        self.selenium.quit()
