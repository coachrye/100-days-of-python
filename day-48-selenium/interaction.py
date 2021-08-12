from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = "http://secure-retreat-92358.herokuapp.com/"

chrome_driver_path = "/Users/coachrye/SeleniumWebDriverProjects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

# driver.find_element_by_link_text()
# click

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Yeba")
first_name = driver.find_element_by_name("lName")
first_name.send_keys("Kast One")
first_name = driver.find_element_by_name("email")
first_name.send_keys("email@email.com")
submit = driver.find_elements_by_css_selector("form button")
submit.click()

driver.quit()