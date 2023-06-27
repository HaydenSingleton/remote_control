from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("send/<data1>/<data2>/<data3>", csrf_exempt(views.send), name="send-data"),
    path("connect", csrf_exempt(views.connect), name="connect"),
]
