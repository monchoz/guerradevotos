from django import forms
from django.forms import ModelForm
from main.models import competitor
from datetime import datetime

class CompetitorForm(ModelForm):
	class Meta:
		model = competitor
