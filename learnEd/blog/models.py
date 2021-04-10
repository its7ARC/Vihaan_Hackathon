from django.db import models
import datetime
from django.utils import timezone
from django.conf import settings
from  django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length = 32)
	pub_date = models.DateTimeField(default = timezone.now)   
	def __str__(self):
		return self.name

class Profile(models.Model):
 	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
 	#UserInfo
 	date_of_birth = models.DateField(blank = True,null = True)
 	photo = models.ImageField(upload_to = 'users/%Y/%m/%d/', blank = True)
 	verified = models.BooleanField(default = False)
 	description = models.TextField(max_length=128,blank = True)
 	employment = models.TextField(max_length=128,blank = True)
 	qualification = models.TextField(max_length=128, blank = True)
 	education = models.TextField(max_length=128,blank = True)
 	#
 	
 	def __str__(self):
 		return 'Profile for user {}'.format(self.user.username)

class Blog(models.Model):
	topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
	preRequisites = models.TextField(max_length = 1024)
	blogContent = models.TextField(max_length = 4096)
	pub_date = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(Profile,on_delete = models.CASCADE)
	verified = models.BooleanField(default = False)
	draft = models.BooleanField(default = False)
	upvote = models.ManyToManyField(Profile,blank = True, related_name = 'upvotes')
 	
	def __int__(self):
		return self.id

class Discuss(models.Model):
	content = models.TextField(max_length = 2048)
	blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
	author = models.ForeignKey(Profile,on_delete = models.CASCADE)

class Bookmark(models.Model):
	blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
	author = models.ForeignKey(Profile,on_delete = models.CASCADE) 
"""
class Upvote(models.Model):
	blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
	author = models.ForeignKey(Profile,on_delete = models.CASCADE) 
	likes=models.ManyToManyField(User,blank=True, related_name='likes')
"""
class SearchLog(models.Model):
	topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
	profile = models.ForeignKey(Profile,on_delete = models.CASCADE)





















