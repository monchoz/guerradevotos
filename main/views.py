from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.template import RequestContext

def login(request):
	if request.user.is_authenticated():
		return redirect('main')
	else:
		return render_to_response('login.html',context_instance=RequestContext(request))

@login_required(login_url='/')
def main(request):
	return render_to_response('main.html',context_instance=RequestContext(request))

@login_required(login_url='/')
def CrearCompetidor(request):
	return render_to_response('crear-competidor.html',context_instance=RequestContext(request))		

@login_required(login_url='/')
def BuscarOponente(request):
	return	 render_to_response('buscar-oponente.html',context_instance=RequestContext(request))