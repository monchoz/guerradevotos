from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# class Competitor(models.Model):
# 	competitor_id = models.AutoField(primary_key=True)
# 	user_id = models.ForeignKey(User)
# 	image = models.ImageField(upload_to='competitors', verbose_name='Image')
# 	name = models.CharField(max_lenght=100, verbose_name='Name')
# 	description = models.CharField(max_lenght=200, verbose_name='Description')
# 	created = models.DateTimeField(auto_now=True, verbose_name='Created')
# 	active = models.IntegerField(max_lenght=1, verbose_name='Active')
