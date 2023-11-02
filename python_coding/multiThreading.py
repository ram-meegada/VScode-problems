import threading
from time import sleep
from email.message import EmailMessage
import smtplib
from datetime import datetime

class SendMail(threading.Thread): 
    def __init__(self, recipient_list):
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)
    def run(self):
        start = datetime.now()
        for i in self.recipient_list:
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

recipient_list = ["kane9014@yopmail.com", "brock9014@yopmail.com", "ram9014@yopmail.com", \
                  "kane29014@yopmail.com", "kane39014@yopmail.com", "kane49014@yopmail.com",\
                  "kane59014@yopmail.com", "kane69014@yopmail.com", "kane79014@yopmail.com", "kane89014@yopmail.com"]
send_mail = SendMail(recipient_list)
send_mail.start()