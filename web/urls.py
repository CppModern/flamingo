from django.urls import path
from . import views


app_name = "web"
urlpatterns = [
    path("home", views.index),
    path("send", views.send_mail)
]
