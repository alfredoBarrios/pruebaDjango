from django.conf.urls import patterns, include, url
from django.contrib import admin

import prueba

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebaDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/$', prueba.views.login), 

)
