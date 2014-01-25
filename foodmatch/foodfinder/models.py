from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

	name = models.CharField(max_length=128)
	phone_number = models.IntegerField(default=1111111111)
	email = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name

class Menu(models.Model):
	dining_hall = models.CharField(max_length=128)

class Food(models.Model):
	menu = models.ForeignKey(Menu)
	name = models.CharField(max_length=128)

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phone = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user.username


