from django.conf.urls import patterns, include, url
from django.contrib import admin
from prueba import views



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebaDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^inicio/$', views.inicio),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'admin/login.html'}, 
        name="AgilePro"),
    
)
