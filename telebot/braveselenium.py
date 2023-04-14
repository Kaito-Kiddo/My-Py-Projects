from selenium import webdriver

driver_path = "C:/Users/username/PycharmProjects/chromedriver.exe"
brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

browser.get("https://www.google.es")