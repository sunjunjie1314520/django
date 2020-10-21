
from django.urls import path, include
from django.http import JsonResponse

from .models import User

def Index(request):
    return JsonResponse({
        'position': 'example MODULE 66666666666666',
    })

urlpatterns = [
    path('', Index),
]