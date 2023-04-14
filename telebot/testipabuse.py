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

def abuse(s):
    ip_dict= {'Source IP' : s}                                  #   Create Dict with first key values of Source IP addr
    # s="103.45.180.152"
    # res=requests.get("https://www.abuseipdb.com/check/"+s)      #   source code of web page
    res=requests.get("https://www.virustotal.com/gui/ip-address/{s}/details")
    res.raise_for_status()
    print(res.text,res.json)
    # soup=bs4.BeautifulSoup(res.text,features="lxml")     

    # # find Confidence and no of times IP reported from ipAbuse soup 
    # ipAbuse=soup.select('div b')        #   Length of ipAbuse List = 17

    # if len(ipAbuse) == 17:
    #     timesReported = ipAbuse[6].get_text() + ' Times'
    #     confidencePercent = ipAbuse[7].get_text()
    # else:
    #     timesReported = 'Not Found'
    #     confidencePercent = 'Not Found'
    # ip_dict.update(zip(['IP reported','Confidence'],[timesReported,confidencePercent]))      # Update Dict 

    # # ip_table contains soup of table tag class table
    # ip_table = soup.find("table", attrs={"class": "table"})     #   get the ip table from website

    # col=[]
    # val=[]
    # i=ip_table.find_all("tr")
    # for j in i:
    #     if j.th.get_text() == 'Hostname(s)':
    #         continue
    #     col.append(j.th.get_text('',strip=True))
    #     val.append(j.td.get_text('',strip=True))
    #     ip_dict.update((zip(col,val)))                 # Update Dict

    # return list(ip_dict.values())                      # return list of dict values

def main():
    ip_list = abuse(input('Enter IP to search : '))
    # print(*ip_list)
if __name__ == '__main__':
    main()