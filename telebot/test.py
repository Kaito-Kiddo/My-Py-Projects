#%%

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains 

# webdrivber wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from selenium import webdriver


import time
driver_path = "C:/Users/kaito/Work Code/Telegram Python Bots/chromedriver.exe"
# brave_path = "C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe"
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
option = webdriver.ChromeOptions()
option.binary_location = edge_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
def testWeb():
    url = f"https://distrowatch.com/"
    driver = webdriver.Edge(executable_path=driver_path, chrome_options=option)
    print("ping before sleep")
    # print(pc.checkPing('google.com'))
    time.sleep(10)
    print("ping after sleep")
    # print(pc.checkPing('google.com'))
    driver.get(url)
    # action = ActionChains(driver) 
    
    driver.quit()
    return url
testWeb()
