'''
now we are adding an attachment along with subject to send email....

'''
import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase # loading the attachment as header file
from email import encoders # encode the file into binary format
# now we can directly insert earlier subject mail code and add the attachment file
From = "ponnadavenakasriharshavardhangmail.com"
To = "ponnadaindia2005@gmail.com"
Subject = "python full stack training - vizag"
body = "we have understood how to send automated emails using python"
attach = "mailsubject.py" # make sure the file is in same location
#now we will add our subject related code
msg = MIMEMultipart()
msg ['From'] = From
msg ['To'] = To
msg ['Subject'] = Subject
msg.attach(MIMEText(body))
# now we need to add attachment to our mail
part = MIMEBase('application','octet-stream')
print(part)
part.set_payload(open(attach).read())
encoders.encode_base64(part)
#lets add the header to our filename
part.add_header('Content-Disposition',f'attachment;filename={os.path.basename(attach)}0')
msg.attach(part) #finally convert this to string
text = msg.as_string()
#include your smtplib code
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("ponnadavenkatasriharshavardhan@gmail.com","lpds nwid yors wmzz")
server.sendmail(From,To,text)
server.quit()
print("mail sent")

