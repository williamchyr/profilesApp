from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth import views as auth_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^accounts/login/$',
            auth_views.login,
            {'template_name': 'registration/login.html'}),
    url(r'^accounts/login_modal/$',
	    auth_views.login,
	    {'template_name': 'registration/login_modal.html'}),
    url(r'^accounts/authenticate/$',
	   'profiles.views.authenticate_user'),
    
    url(r'^accounts/', include('registration.urls')),   
    url(r'^$', 'profiles.views.index'),
    url(r'^index2$', 'profiles.views.index2'),
)
