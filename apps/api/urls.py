
from django.urls import path, include
from django.http import JsonResponse

from .models import Person

def Index(request):
    return JsonResponse({
        'position': 'API MODULE',
    })

urlpatterns = [
    path('', Index),
    path('/users/', include('users.urls')),
    path('/operation/', include('operation.urls')),
    path('/message', include('message.urls')),
    path('/barber', include('barber.urls')),
]