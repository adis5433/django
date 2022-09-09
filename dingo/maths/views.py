from django.shortcuts import render
from django.http import HttpResponse


def math(request):
    return HttpResponse("Tu odbywać się będzie matma")


def add(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a+b)


def sub(request, a, b):
    a, b = int(a), int(b)
    return HttpResponse(a-b)


def mul(request, a,b):
    a, b = int(a), int(b)
    return HttpResponse(a*b)

def div(request, a,b):
    a, b = int(a), int(b)
    if b == 0:
        return HttpResponse('Niedziel przez zero!')
    return HttpResponse(a/b)


# Create your views here.
