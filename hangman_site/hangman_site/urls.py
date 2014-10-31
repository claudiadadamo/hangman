from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hangman_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hangman/', include('hangman.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
