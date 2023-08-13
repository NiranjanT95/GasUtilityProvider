from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView
from django.contrib.staticfiles.views import serve
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.conf import settings
import os
# Create your views here.
class RequestsView(LoginRequiredMixin, ListView):
    login_url = "/login/"
    template_name = "requests.html"
    model = Request
    context_object_name = 'requests'
    def post(self, request):
        req_type = request.POST.get('req_type')
        req_subject = request.POST.get('req_subject')
        file  = request.FILES["file"]
        request = Request(file = file, req_type = req_type, req_subject = req_subject, user = request.user, status="Active")
        request.save()
        return HttpResponseRedirect("/requests/?alert=true")
    def get_queryset(self):
        data = Request.objects.filter(user = self.request.user)
        return data

class FileView(LoginRequiredMixin, View):
    def get(self, request, file_name):
        return serve(request, os.path.basename("files/"+file_name), os.path.dirname("files/"+file_name))