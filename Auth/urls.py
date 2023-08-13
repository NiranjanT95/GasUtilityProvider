from django.urls import path
from .views import *
from RequestHandler.views import RequestsView
urlpatterns = [
     path('login/', LoginPageView.as_view(), name = 'login'),
     path('', RequestsView.as_view(), name = 'requests_view'),
     path('account/', AccountDetailView.as_view(), name='account')
]