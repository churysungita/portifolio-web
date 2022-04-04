from django.shortcuts import render

from django.conf import settings

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html')