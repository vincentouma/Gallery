from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.


def welcome(request):
    return render(request, "welcome.html")
