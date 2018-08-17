from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users
import smtplib

def send(request):
   gmail_user = 'vajjaprasanth123@gmail.com'
   gmail_pwd = 'Prasanth@123'
   FROM = gmail_user
   address = Users.objects.all().last()
   recipient = address.emailId

   print("address:",address.emailId)
   TO = recipient if type(recipient) is list else [recipient]
   SUBJECT = 'email test'
   TEXT = 'succesfully registered as a user in our app'
   message = """From: %s\nTo: %s\nSubject: %s\n\n%s
   """% (FROM, ", ".join(TO), SUBJECT, TEXT)
   try:
       server = smtplib.SMTP("smtp.gmail.com", 587)
       server.ehlo()
       server.starttls()
       server.login(gmail_user, gmail_pwd)
       server.sendmail(FROM, TO, message)
       server.close()
       return HttpResponse("success")
   except Exception as ex:
       return HttpResponse(ex)
# Create your views here.
