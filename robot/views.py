from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

import socket
import struct

ROBOT_ADDRESS = ('192.168.2.211', 0)

# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html")

@require_POST
def send(request: HttpRequest, data1, data2, data3):

    print("Sending:", data1, data2, data3)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as robot:
        robot.connect(ROBOT_ADDRESS)

        msg = struct.pack('<3d', data1, data2, data3)
        robot.sendall(msg)

    return HttpResponse("ok")