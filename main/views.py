from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from main.forms import CompetitorForm
from django.shortcuts import redirect
from django.template import RequestContext
from social_auth.models import UserSocialAuth
from main.models import competitor
from django.core import serializers
from django.utils import simplejson
from django.contrib.auth.models import User

def GetRegisteredUsers(maxResults=0, startsWith=''):
	usersList = []
	if startsWith:
		usersList = User.objects.filter(first_name__istartswith=startsWith, is_staff=0).values('id','first_name','social_auth__uid').order_by('first_name')
	else:
		usersList = User.objects.filter(is_staff=0).values('id','first_name','social_auth__uid').order_by('first_name')
	if maxResults > 0:
		if len(usersList) > maxResults:
			usersList = usersList[:maxResults]
	return usersList

def SearchUsers(request):
	context = RequestContext(request)
	usersList = []
	startsWith = ''
	if request.method == 'GET':
	        startsWith = request.GET['userName']

	usersList = GetRegisteredUsers(8, startsWith)

	return render_to_response('users-list.html', {'usersList': usersList}, context)

def login(request):
	if request.user.is_authenticated():
		return redirect('main')
	else:
		return render_to_response('login.html',context_instance=RequestContext(request))

@login_required(login_url='/')
def AddCompetitor(request):
	if request.is_ajax():
		if reques.method == 'POST':
			competitorFrm = CompetitorForm(data=request.POST)
			if competitorFrm.is_valid():
				u = competitorFrm.save(commit=false)
				u.user = request.user.id
				u.created = datetime.now()
				u.active = 1
				u.save()
				result = {'code': 1, 'msg': 'Competidor se creo correctamente'}
				return HttpResponse(simplejson.dumps(result))
			else:
				result = {'code': 2, 'msg': 'Ocurrio un problema al intentar crear competidor'}
				return HttpResponse(simplejson.dumps(result))

@login_required(login_url='/')
def main(request):
	return render_to_response('main.html',context_instance=RequestContext(request))

@login_required(login_url='/')
def CrearCompetidor(request):
	return render_to_response('crear-competidor.html',context_instance=RequestContext(request))		

@login_required(login_url='/')
def CrearDuelo(request):
	context = RequestContext(request)
	usersList = []
	usersList = User.objects.filter(is_staff=0).values('id','first_name','social_auth__uid').order_by('first_name')
	usersList = usersList[:20]
	return	render_to_response('crear-duelo.html', {'usersList': usersList}, context)

@login_required(login_url="/")
def log_out(request):
	logout(request)
	return redirect('home')
