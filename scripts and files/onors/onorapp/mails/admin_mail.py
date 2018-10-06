import smtplib
from onorapp.models import Registers
from django.http import JsonResponse
import email.mime.application
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




class admin_mail():
    def __init__(self):
        pass

    def send(mail_id):

       gmail_user = 'onor.register@gmail.com'
       gmail_pwd = 'Sprite123$'
       user=Registers.objects.all().last()
       details={"first_name":user.first_name,"last_name":user.last_name,'mobile_no':user.mobile_no,"email":user.email,
                "enquiry":user.enquiry,"file":user.file,"acknowledge":user.acknowledge,"acknowledge_by":user.acknowledge_by,"status":user.status}
       FROM = gmail_user
       recipient = mail_id
       TO = recipient if type(recipient) is list else [recipient]
       SUBJECT = 'Enquiries'
       TEXT = ('you got an enquiry from:  ',details)
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
