from django.db import models

# Create your models here.
class students(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.TextField()

class newsletter(models.Model):
    email=models.EmailField()

class Subjects(models.Model):
    title=models.CharField(max_length=200)
    title1=models.CharField(max_length=200)
    title2=models.CharField(max_length=200)
    title3=models.CharField(max_length=200)
    title4=models.CharField(max_length=200)
    title5=models.CharField(max_length=200)
    image=models.ImageField(upload_to='img')
    image1=models.ImageField(upload_to='img')
    image2=models.ImageField(upload_to='img')
    image3=models.ImageField(upload_to='img')
    image4=models.ImageField(upload_to='img')
    image5=models.ImageField(upload_to='img')
    short_des=models.TextField()
    detail_des=models.TextField()
    detail_des1=models.TextField()
    detail_des2=models.TextField()
    detail_des3=models.TextField()
    detail_des4=models.TextField()
    detail_des5=models.TextField()
    
