"""     IP addr details using AbuseIPdb.com

This script allows the user to 
open a website https://www.abuseipdb.com/check/ and check the abuse of a given IP addr

save the result like source IP, ISP, Country, Abuse Confidence % and no of times IP was reported to a Dictionary.

Return that dictionary
"""
#%%
import webbrowser
import requests
import bs4
import openpyxl
import ipaddress as ip

def abuse(s):
    ip_dict= {'Source IP' : s}                                 #   Create Dict with first key values of Source IP addr
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    url=f"https://www.abuseipdb.com/check/{s}"
    res=requests.get(url,headers=headers)      #   source code of web page

    res.raise_for_status()
    
    soup=bs4.BeautifulSoup(res.text,features="html.parser")     

    # find Confidence and no of times IP reported from ipAbuse soup 
    ipAbuse=soup.select('div b')        #   Length of ipAbuse List = 17

    if len(ipAbuse) == 17:
        timesReported = ipAbuse[6].get_text() + ' Times'
        confidencePercent = ipAbuse[7].get_text()
    else:
        timesReported = 'Not Found'
        confidencePercent = 'Not Found'
    ip_dict.update(zip(['IP reported','Confidence'],[timesReported,confidencePercent]))      # Update Dict 

    # ip_table contains soup of table tag class table
    ip_table = soup.find("table", attrs={"class": "table"})     #   get the ip table from website

    col=[]
    val=[]
    i=ip_table.find_all("tr")
    for j in i:
        if j.th.get_text() == 'Hostname(s)':
            continue
        col.append(j.th.get_text('',strip=True))
        val.append(j.td.get_text('',strip=True))
        ip_dict.update((zip(col,val)))                 # Update Dict

    return ip_dict                      # return list of dict values

def main():
    ip_addr = ip.ip_address(input('Enter IP to search : '))
    if ip_addr.is_global : 
        ip_dict = abuse(str(ip_addr))   # abuse function accepts a string value and ip_addr is ipaddress object
        for key,value in ip_dict.items():
            print(key, ':', value)
    else : 
        fs = f"{ip_addr} is not global IPv4 Addr"
        print(fs)
        
if __name__ == '__main__':
    main()