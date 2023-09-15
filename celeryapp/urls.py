from django.urls import path
from celeryapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('mail/', views.simple_mail, name='simple_mail')
]