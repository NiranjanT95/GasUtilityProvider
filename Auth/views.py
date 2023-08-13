from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from . import forms
from django.views.generic import View, DetailView
from .models import *

class LoginPageView(View):
    template_name = 'login.html'
    form_class = forms.LoginForm
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('/')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})
    
class AccountDetailView(LoginRequiredMixin, View):
    def get(self, request):
        if not request.user.is_superuser:
            return render(request, "account_detail.html", {'account':AccountDetail.objects.filter(user = request.user)[0]})
        else:
            return HttpResponseRedirect('/admin/')