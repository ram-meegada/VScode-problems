from email.message import EmailMessage
import smtplib
import threading
from datetime import datetime

def send_mail():
    start = datetime.now()
    for i in ["kane9014@yopmail.com", "brock9014@yopmail.com", "ram9014@yopmail.com", \
              "kane29014@yopmail.com", "kane39014@yopmail.com", "kane49014@yopmail.com",\
              "kane59014@yopmail.com", "kane69014@yopmail.com", "kane79014@yopmail.com", "kane89014@yopmail.com"]:
        email_id = 'stefenwarner13@gmail.com'
        email_pass = 'iyutbwcpmhehhmuc'
        msg = EmailMessage()
        msg['Subject'] = 'this is subject'
        msg['From'] = email_id
        msg['To'] = f"{i}"
        msg.set_content("this is testing message")
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as mail:
            mail.login(email_id, email_pass)
            mail.send_message(msg)
    print(datetime.now()-start, 'done---------')

send_mail()