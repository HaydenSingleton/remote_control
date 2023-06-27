from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

import socket
import struct

# Create your views here.

def index(request: HttpRequest):

    return render(request, "index.html")

robot = None

@require_POST
def send(req, data1, data2, data3):

    msg = struct.pack('<3d', float(data1), float(data2), float(data3))
    robot.sendall(msg)

    return HttpResponse()


@require_POST
def connect(req):
    robot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    robot.connect(('192.168.2.211', 18005))
    return HttpResponse()
