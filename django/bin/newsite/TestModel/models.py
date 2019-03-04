from django.db import models

# Create your models here.
class eaxm_db(models.Model):
	name = models.CharField(max_length = 20)
	address = models.CharField(max_length = 20, default = "")
	phone = models.IntegerField(default = 0)

class Contact(models.Model):
	name = models.CharField(max_length = 200)
	age = models.IntegerField(default = 0)
	email = models.EmailField()
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	contact = models.ForeignKey(Contact)
	name = models.CharField(max_length = 50)
	def __unicode__(self):
		return self.name