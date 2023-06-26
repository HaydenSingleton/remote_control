from django.shortcuts import render

from django.http import HttpRequest
from django.shortcuts import render
# from django.views.decorators.http import require_POST

# Create your views here.
def index(request: HttpRequest):
    return render(request, "index.html")
