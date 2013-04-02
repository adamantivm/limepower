from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.http import HttpResponse

urlpatterns = patterns('',
    url(r'^$', 'lime.views.index'),
)
