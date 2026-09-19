'''
python --> automation-->email automation --> google mail

simple mail automation
mail OTP
mail with subject&attachments
bulk mail

simple mail automation
------------------------
SMTP --> simple mail transfer protocol


import smtplib
#first lets make server connection
server = smtplib.SMTP('smtp.gmail.com',587)
#print(server)
#start the connection
server.starttls()
#login
server.login("ponnadavenkatasriharshavardhan@gmail.com","lpds nwid yors wmzz")
msg = "hello"
server.sendmail("ponnadavenkatasriharshavardhan@gmail.com","garaprasad116@gmail.com",msg)
#close the connection
server.quit()
print("mail sent")

now lets send OTP to mail and validate the script
'''
import math
import random
import smtplib

#digits = '1234567890'
#OTP = ""
#for i in range(4):
#    OTP += digits[math.floor(random.random()*10)]
#    print(OTP)

otp = random.randint(1000,9999)
#print(otp)
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
msg = f'hello this is harsha {otp}'
#login
server.login("ponnadavenkatasriharshavardhan@gmail.com","lpds nwid yors wmzz")
server.sendmail("ponnadavenkatasriharshavardhan@gmail.com","garaprasad116@gmail.com",msg)
#close the connection
server.quit()
print("mail sent")
OTP = int(input('enter your otp: '))
if OTP == otp :
    print("success")
else:
    print("not success")

