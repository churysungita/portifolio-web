from multiprocessing import context
from django.shortcuts import render

from django.conf import settings
from .models import project
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    project=project.objects.all()
    context={
        "myproject":project
    }
    return render(request, 'index.html',context)
  