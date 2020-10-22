
from django.urls import path, include
from django.http import JsonResponse

from .models import User

def Index(request):
    return JsonResponse({
        'position': 'example MODULE',
        'msg': 'success',
    })

urlpatterns = [
    path('', Index),
]