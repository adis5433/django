from django.shortcuts import render
from django.http import HttpResponse


def greet(request):
    return HttpResponse(f"Hello World")


def greet_by_name(request, name):
    return HttpResponse(f"Hello {name.capitalize()}!")
# Create your views here.
