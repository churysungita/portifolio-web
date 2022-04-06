from turtle import title
from django.db import models

# Create your models here.

class project (models.Model):
    title=models.CharField(max_length=50)
    text=models.TextField(max_length=100)
    project_image=models.ImageField(upload_to='media/')
    
    link=models.URLField(max_length=50)

    def _str_(self):
        return self.title