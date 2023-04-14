"""

    script to automate 
    modfem configuration

    it takes landline number as input
    if more than 1 connection is registered on given number 
    then it asks to input which credential to choose



"""


#%% 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.action_chains import ActionChains 

# webdrivber wait imports
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# local imports
import modem_searchXL as ms


#%%
def configure(mpass='admin',user_name='nicdelhi_dgb@nic',pass_word='anil$789'):

    modem_pass=mpass
    url = f"http://admin:{modem_pass}@192.168.1.1"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.get("http://192.168.1.1/basic/home_wan.htm")
    action = ActionChains(driver) 

    # nicdelhi landline - 23392411


    username = user_name
    # input("Enter Username : ")
    password = pass_word
    # input("Enter password : ")
    element = driver.find_element_by_name("wan_PPPUsername")
    element.clear()
    element.send_keys(username)


    element = driver.find_element_by_name("wan_PPPPassword")
    element.clear()
    element.send_keys(password)
    element = driver.find_element_by_name("SaveBtn")
    action = ActionChains(driver) 
    action.move_to_element(element).click().perform()


    # change dns in lan go to this page
    # http://192.168.1.1/basic/home_lan.htm

    driver.get('http://192.168.1.1/basic/home_lan.htm')
    dns_p ='10.1.16.207'
    dns_s ='10.1.16.208'

    # get element of p n s dns
    element = driver.find_element_by_name("uiViewDns1Mark")
    element.clear()
    element.send_keys(dns_p)

    element = driver.find_element_by_name("uiViewDns2Mark")
    element.clear()
    element.send_keys(dns_s)

    element = driver.find_element_by_name("SaveBtn")
    action = ActionChains(driver) 
    action.move_to_element(element).click().perform()

    #for sysrestart go to
    # http://192.168.1.1/maintenance/tools_system.htm 

    driver.get('http://192.168.1.1/maintenance/tools_system.htm')

    element = driver.find_element_by_name("Restart")
    action = ActionChains(driver) 
    action.move_to_element(element).click().perform()

    # wait till restart hits 100%
    try:
        element = WebDriverWait(driver, 55).until(
        EC.text_to_be_present_in_element((By.NAME, "FWTrendValue"), "100%")
        )

    finally:
        driver.close()
        driver = webdriver.Chrome()
        url = f"http://admin:{modem_pass}@192.168.1.1/status/status_deviceinfo.htm"
        # url = f"http://admin:{modem_pass}@192.168.1.1"
        driver.get(url)
 
        # xpath of status not / connected
        # /html/body/form/table[2]/tbody/tr[3]/td[5]
        # status_text = driver.find_elements_by_xpath("/html/body/form/table[2]/tbody/tr[3]/td[5]")
        # print(*status_text, sep = ", ")
    
    

#%%
def main():
    u , p = ms.searchUP(input('Enter your registered mtnl landline number : '))
    print(u , p)
    mpass = 'admin'
    configure(mpass,u,p)

if __name__ == '__main__':
    main()