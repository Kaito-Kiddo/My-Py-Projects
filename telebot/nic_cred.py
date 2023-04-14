"""
Search NIC username and Passwird for a given MTNL landline number and returns them
"""

#%%
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
    
def searchUP(pno):    
    # pno = input('Enter your registered mtnl landline number : ')
    pno=pno
    print(pno)
    df = pd.read_excel('BList.xlsx', sheet_name='Delhi Gov')
    
    print("Column headings:")
    print(df.columns)

    filt = ( df['Phone no'] == pno )
    print(filt)

    # un contains username dataframe
    un = df.loc[filt, 'User Name'].values
    u_index = 0
    if len(un) > 1 :
        for (i,item) in enumerate(un):
            print(i," ",item)
        u_index = int(input("enter index - "))
    uname = un[u_index]
    # print(uname)
    # pwd contains password of un
    pwd = df.loc[filt,'Password'].values
    p_index = 0
    if len(pwd) > 1 :
        for (i,item) in enumerate(pwd):
            print(i," ",item)
        p_index = int(input("enter index - "))
    passwd = pwd[p_index]
    # print(passwd)
    return [uname,passwd]

def main():
    uname , passwd = searchUP(input('Enter your registered mtnl landline number : '))
    print("Your Username - ",uname,"Password - ",passwd,sep="")

if __name__ == '__main__':
    main()