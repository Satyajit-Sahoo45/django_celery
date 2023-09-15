from celery import shared_task
from time import sleep
from django.core.mail import send_mail

@shared_task
def mail_send():
    sleep(10)
    send_mail(subject="Hi this is subject field",
              message = "this is body field",
              from_email="satyajit.sahoo1@hyscaler.com",
              recipient_list=["sahoosatyajit2801@gmail.com"])
    return "mail sent"