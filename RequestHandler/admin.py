from django.contrib import admin
from .models import *
# Register your models here.
class RequestView(admin.ModelAdmin):
    list_display = ['user', 'req_type', 'status', 'creation_datetime']
admin.site.register(Request,RequestView)
