#%%
import smtplib
import os
from email.message import EmailMessage
def mail(Msub='Attachment!',Mto='shashi200791@gmail.com'):
    EMAIL_ADDRESS = os.getenv('DB_USER')
    EMAIL_PASSWORD = os.getenv('DB_PASS') 
    # print(EMAIL_ADDRESS,EMAIL_PASSWORD)
    files = ['demoxl.xlsx','demoHello.txt']
    msg = EmailMessage()
    msg['Subject'] = Msub
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = Mto

    msg.set_content('Please Find the attached files')
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == '__main__':
    mail()