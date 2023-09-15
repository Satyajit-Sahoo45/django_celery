from django.shortcuts import render
from .tasks import mail_send
from django.http import HttpResponse

def simple_mail(request):
    mail_result = mail_send.delay()
    print("Mail Result", mail_result)
    return render(request, "mail.html")

def index(request):
    return render(request, "home.html")
