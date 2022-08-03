import requests
import smtplib
import os

Email_Address = os.environ.get('Email_Address')
Email_Password = os.environ.get('Email_Password')

def send_notification(email_msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(Email_Address, Email_Password)
        mssg = f"Subjecr: Site Down\n{email_msg}"
        smtp.sendmail(Email_Address, Email_Password, mssg)

try:
    response = requests.get('https://www.bankofbaroda.in/')
    if response.status_code == 200:
        print('Application is running successfully')
    else:
        print('Application Down. Fix it!')
        msg = f'Application returned {response.status_code}'
        send_notification(msg)
except Exception as ex:
    print(f'Connection error happened: {ex}')
    msg = 'Application not accessible at all'
    send_notification(msg)