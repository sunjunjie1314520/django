
from django.urls import path, include
from django.http import JsonResponse

from .models import User

def Index(request):
    return JsonResponse({
        'position': 'example MODULE',
        'msg0': 'success',
        'msg1': 'success',
        'msg2': 'success',
        'msg3': 'success',
    })

urlpatterns = [
    path('', Index),
]