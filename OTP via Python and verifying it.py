import random
import pymysql
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
sql=pymysql.connect("46.4.115.158", "root", "Mysql@rhombus123", "demo")
x=sql.cursor()
name=input("Enter the name:")
#print(name)
email=input("Enter the mail id:")
#print(email)
mobilenuber=input("Enter the mobile number:")
#print(mobilenuber)
otp=random.randint(1,10000)
otp1=str(otp)
date=localtime=time.asctime(time.localtime(time.time()))
a=localtime.split()
b=a[3]

#print(type(otp))
#try:
x.execute("""INSERT INTO OLA values(%s,%s,%s,%s)""",(name,mobilenuber,b,otp))
print("Sucessfully")

me = "Enter the senders mail id"
you = "Enter the recievres mail id"

 # Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Data has Arrived"
msg['From'] =me
msg['To'] = you
text="Hi this is your OTP"+otp1
part1=MIMEText('plain'+text)
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('sender mail id','password')
mail.sendmail(me, you, msg.as_string())
cur = sql.cursor()

cur.execute("SELECT OTP , name FROM OLA")
row = cur.fetchone()
while row is not None:
    print(row[x])
    row = cur.fetchone()
    print(row)

cur.close()
sql.commit()
sql.close()
mail.quit()

#except:
    #sql.rollback()
    #print("It is not sucessfull")'''
