#!/usr/bin/python

import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login('sender_email, 'account_password')

try:
	smtpObj.sendmail('sender_email', 'receiver_email', 'Subject: So,Bob')
	print "Successfully sent email"
except:
	print "email not sent"

smtpObj.quit()