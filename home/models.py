from django.db import models

# Create your models here.
class Customers(models.Model):
     name=models.CharField(max_length=100)
     img=models.ImageField(upload_to='pics')
     desc=models.TextField(null=True,blank=True)
     links=models.CharField(max_length=500,default="https://www.wikipedia.org/")
     polarity=models.FloatField()
     subjectivity=models.FloatField()
