from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.http import HttpResponse
import logging

logger = logging.getLogger('server.views')

def server_login(request):
    logger.info("logging in user %s" % request.POST['username'])
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return HttpResponse('Login error, try again')
