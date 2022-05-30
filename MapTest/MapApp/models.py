from django.db import models
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Concert(models.Model):
    
    introduce = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    latitude = models.TextField()  # 위도
    logitude = models.TextField() # 경도

    # 즐겨찾기 여부

 