from django.db import models

# Create your models here.
class  Footer(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=32, null=False)
    link = models.URLField(max_length=255,null=False)
    isdisplay = models.BooleanField(default=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class SiteInfo(models.Model):
    siteName = models.CharField(max_length=64,primary_key=True)
    siteFlag = models.CharField(max_length=32)
    isValid = models.BooleanField(default=True)
    description = models.CharField(max_length=32)

