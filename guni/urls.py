from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'guni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #url(r'^$', 'core.views_old.home', name='home'),
    url(r'^testes/', include('core.urls', namespace="url")),
    url(r'^admin/', include(admin.site.urls)),
)
#urlpatterns += staticfiles_urlpatterns()
