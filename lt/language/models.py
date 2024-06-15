from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class signup(models.Model):
	userid=models.AutoField(primary_key=True)
	username=models.CharField(max_length=200)
	email=models.CharField(max_length=150)
	dob=models.DateField(null=True)
	registerdate=models.DateTimeField(auto_now=True)
	password=models.CharField(max_length=128)

class login(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	time=models.DateTimeField(auto_now=True)
	aspect=models.CharField(max_length=10,default="login")

class transalate(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=200)
	fromlang=models.TextField()
	tolang=models.TextField()
	fromtext=models.TextField()
	totext=models.TextField()
	date=models.DateTimeField(auto_now=True)

class translation(models.Model):
	id=models.AutoField(primary_key=True)
	fromlang=models.CharField(max_length=200)
	tolang=models.TextField()
	fromtext=models.TextField()
	totext=models.TextField()
	date=models.DateTimeField(auto_now=True)

class feedback(models.Model):
	id=models.AutoField(primary_key=True)
	date=models.DateTimeField(auto_now=True)
	query=models.TextField()
	comment=models.TextField()
	rating=models.IntegerField()

class feedbackt(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=10)
	date=models.DateTimeField(auto_now=True)
	query=models.TextField()
	comment=models.TextField()
	rating=models.IntegerField()

class audio(models.Model):
	audioname=models.CharField(max_length=100)
	audio=models.FileField(upload_to='audio')
	def __str__(self):
		return self.audioname

class quotes(models.Model):
	image=models.ImageField(upload_to='images/')
	text=models.TextField()

class quotesg(models.Model):
	image=models.ImageField(upload_to='images/')
	name=models.TextField()
	text=models.TextField()

class superuser(models.Model):
	userid=models.AutoField(primary_key=True)
	username=models.CharField(max_length=200)
	email=models.CharField(max_length=150)
	dob=models.DateField(null=True)
	registerdate=models.DateTimeField(auto_now=True)
	password=models.CharField(max_length=128)

class superuserlogin(models.Model):
	id=models.AutoField(primary_key=True)
	username=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	time=models.DateTimeField(auto_now=True)
	aspect=models.CharField(max_length=10,default="login")