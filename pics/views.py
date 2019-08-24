from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt

# Create your views here.


def gallery(request):
    date = dt.date.today()
    pics = Image.gallery()
    return render(request, 'all-pics/gallery.html', {"date": date,"news":news})

