from multiprocessing import context
from django.shortcuts import render

from django.conf import settings
from .models import project
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
   
    p1=project.objects.all()
    
    context={
        "myproject":p1
    }
    return render(request, 'index.html',context)
  