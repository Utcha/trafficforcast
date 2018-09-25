from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=2048)
    reg_date = models.DateTimeField(auto_created=True, auto_now=True)

class RoadData(models.Model):
    date = models.CharField(max_length=32)
    hour = models.CharField(max_length=16)
    start_id = models.CharField(max_length=64)
    end_id = models.CharField(max_length=64)
    pass_time = models.CharField(max_length=16)