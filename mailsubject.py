'''
in this case we need to add subject and to address for mail

we will use email package

'''
import email
import smtplib
#MIME --> multipurpose internet mail extension
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# now we will provide the details
From = "ponnadavenkatasriharshavardhan@gmail.com"
To = "garaprasad116@gmail.com"
subject = " python full stack training"
#now we will check all the details and throw it to multipart
msg = MIMEMultipart()
#print(msg)
#print(type(msg))
msg['From'] = From
msg['To']= To
msg['subject']=subject
msg['body']= "hey guys, what's the plan for this week"
msg.attach(MIMEText(msg['body'],'plain'))
text=msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
#login
server.login(From,"lpds nwid yors wmzz")
server.sendmail(From,To,text)
#close the connection
server.quit()
print("mail sent")
