from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'miProyecto.views.home', name='home'),
     url(r'^$', 'demo.views.home', name='home'),
     url(r'^hola/$', 'demo.views.hola', name='hola'),
     url(r'^adios/$', 'demo.views.adios', name='adios'),
     url(r'^aprendiendo/$', 'demo.views.aprendiendo', name='aprendiendo'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
