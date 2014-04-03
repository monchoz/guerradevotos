from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class competitor(models.Model):
	competitor_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to='competitors', verbose_name='Image')
	name = models.CharField(max_length=100, verbose_name='Name')
	description = models.CharField(max_length=200, verbose_name='Description')
	created = models.DateTimeField(auto_now=True, verbose_name='Created')
	active = models.IntegerField(max_length=1, default='1', verbose_name='Active', editable=False)

	def __unicode__(self):
		return self.name
