import smtplib

class SendMail():
    def __init__(self):
        pass

    def send(mail_id):
        """send mail"""
        gmail_user = 'bhanuchander008@gmail.com'
        gmail_pwd = 'abhi1015'
        FROM = gmail_user
        #address = Users.objects.all().last()
        recipient = mail_id
        #print("address:",address.Email)
        TO = recipient if type(recipient) is list else [recipient]
        SUBJECT = 'USER REGISTRATION'
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
            return ("success")
        except Exception as ex:
            return (ex)
