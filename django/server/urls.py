from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.http import HttpResponse

# Adding a new Socket.IO Namespace:
# 1- Import the namespace Class here (where the code actually is)
# 2- Add it to the second parameter to socketio_manage below
from lime.socket import LimeNamespace

from socketio import socketio_manage

def socketio_hookup(request):
    socketio_manage(request.environ, {LimeNamespace.name: LimeNamespace}, request)
    return HttpResponse("Socket connection ended")

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Make the default go straight to static HTMLs
    url(r'^$', RedirectView.as_view(url="/static/index.html"), name="index"),
    url(r'^login$', 'server.views.server_login'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Connect to socketio namespace
    url(r'^socket\.io', socketio_hookup),
)
