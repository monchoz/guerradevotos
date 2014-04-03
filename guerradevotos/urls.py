from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from social_auth.backends import get_backend
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('social_auth.urls')),  
    url(r'^$', 'main.views.login', name='home'),
    url(r'^login/$', RedirectView.as_view(url='/login/facebook')),
    url(r'^main/$', 'main.views.main', name='main'),
    url(r'^crear-duelo/$', 'main.views.CrearDuelo', name='CrearDuelo'),
    url(r'^crear-duelo/agregar-nuevo/$', 'main.views.IngresarCompetidor', name="IngresarCompetidor"),
    url(r'^log_out/$', 'main.views.log_out'),
    url(r'^users-list/$', 'main.views.SearchUsers', name='SearchUsers'),
    url(r'^admin/', include(admin.site.urls)),
 	) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
