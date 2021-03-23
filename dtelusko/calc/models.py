from django.db import models
from datetime import datetime
from time import strftime
import datetime as dt
# Create your models here.
class Log(models.Model):
    idNumber = models.CharField(max_length=15)
    in_time=models.DateTimeField(default=datetime.now())
    out_time= models.DateTimeField(null=True)
    def __str__(self):
        return self.idNumber
