
from django.urls import path, include
from django.http import JsonResponse

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/users/', include('users.urls')),
    path('/operation/', include('operation.urls')),
    path('/message', include('message.urls')),
    path('/barber', include('barber.urls')),
    path('/example', include('example.urls')),
    path('/applets', include('applets.urls')),
]