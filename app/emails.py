from flask_mail import Message

from . import mail

def send_email(email_obj, to):
    
    msg = Message(subject = email_obj['email_subject'], body= email_obj['email_body'], recipients= [to] )
    mail.send(msg)

