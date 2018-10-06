import smtplib
from django.http import JsonResponse
import email.mime.application
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import random
from random import randint
#from onorapp.Controllers.User import ForgotPassword
class forgotpassword_mail():
   def __init__(self):

       pass
   def send(mail_id,num):
        gmail_user = 'manyamraghuram@gmail.com'
        gmail_pwd = 'bargav@teja'
        FROM = gmail_user
        recipient = mail_id
        TO = recipient if type(recipient) is list else [recipient]

        SUBJECT = 'Forgot Password'
        TEXT = ('OTP for for your account is:', num)
        message = """From: %s\nTo: %s\nSubject: %s\n\n%s
        """% (FROM, ", ".join(TO), SUBJECT, TEXT)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(gmail_user, gmail_pwd)
            server.sendmail(FROM, TO, message)
            server.close()
            return ("success")
        except Exception as ex:
            return (ex)
