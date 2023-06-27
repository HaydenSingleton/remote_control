from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

import socket
import struct


# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html")

ROBOT_ADDRESS = ('192.168.2.211', 9999)

@require_POST
def send(request: HttpRequest, data1, data2, data3):

    print("Sending:", data1, data2, data3)

    try:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as robot:
            robot.connect(ROBOT_ADDRESS)

            msg = struct.pack('<3d', data1, data2, data3)
            robot.sendall(msg)
            print(msg)

        return HttpResponse("ok")
    except OSError:
        return HttpResponse("failed")