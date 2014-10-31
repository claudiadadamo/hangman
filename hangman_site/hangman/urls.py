from django.conf.urls import patterns, url
from django.contrib import admin

from hangman import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

# urlpatterns = patterns('',
#     url(r'^hangman/', include(hangman.urls)),
#     url(r'^admin/', include(admin.site.urls)),
# )