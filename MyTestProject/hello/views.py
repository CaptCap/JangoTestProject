from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requests):
    return HttpResponse("Hello, Moto")
def wes(request):
    return HttpResponse("Hello, Wes!")

def greet(requests, name):
    return HttpResponse(f"Hello, {name}")