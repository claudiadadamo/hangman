from django.conf.urls import patterns, url
from django.contrib import admin

from hangman import views


urlpatterns = patterns('',
    url(r'index.html', views.index, name='index'),
    url(r'get_guess/$', views.get_guess, name='get_guess'),
)

# urlpatterns = patterns('',
#     url(r'^hangman/', include(hangman.urls)),
#     url(r'^admin/', include(admin.site.urls)),
# )