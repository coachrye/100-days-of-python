from selenium import webdriver

# URL = "https://www.amazon.ca/LG-34UM69G-B-34-UltraWide-Reduction/dp/B06XFXX5JH"
URL = "http://python.org"

chrome_driver_path = "/Users/coachrye/SeleniumWebDriverProjects/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(URL)

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name()
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# driver.find_element_by_css_selector(".documentation-widget a")

#  XPATH
# events_link = driver.find_element_by_xpath('//*[@id="events"]/a')
# events_link.click()

# //*[@id="content"]/div/section/div/div/ul
# //*[@id="content"]/div/section/div/div/ul/li[1]
# //*[@id="content"]/div/section/div/div/ul/li[2]

# MULTIPLE ELEMENT FIND
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)
# active tab
driver.close()

# entire browser
driver.quit()
