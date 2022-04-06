from . import views
from django.urls import path 

app_name= 'portifolioapp'

urlpatterns = [
    
    path('', views.index , name ='index'),
    
]