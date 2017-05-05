from django.shortcuts import render;
from django.template import RequestContext
from django.views import View;
from django.http import HttpResponseRedirect, HttpResponse;
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    );
# Create your views here.

class TimelineView(View):
    '''Handles Request to view Timeline'''

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            context = { 'user':request.user.username } 
            return render(request, 'timeline/timeline.html', context=context);
        else:
            return HttpResponseRedirect('/login/')

class TimelineLogin(View):
    '''Handles Request to Login to View Timeline'''

    def post(self, request, *args, **kwargs):
        context = RequestContext(request);
        username = request.POST['username'];
        password = request.POST['password'];

        user = authenticate(username = username, password=password);

        if user:
            if user.is_active:
                login(request, user);
                return HttpResponseRedirect('/timeline/');
            else:
                return HttpResponse("Your Account was Deactivated");
        else:
            return HttpResponse("Invalid Login details supplied")

    def get(self, request, *args, **kwargs):
        context = RequestContext(request);
        return render(request, 'timeline/login.html')


class TimelineLogout(View):
    ''''Logs User Out'''
    def get(self, request, *args, **kwargs):
        logout(request);
        return HttpResponseRedirect('/login/'); 
