from django.conf.urls import patterns, include, url
from django.contrib import admin
from prueba.views import myLogin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebaDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', myLogin, {'template_name': 'login.html'}),
    
    
)
