
from django.urls import path, include
from django.http import JsonResponse

from .models import Person

def Index(request):
    return JsonResponse({
        'position': '首页',
    })

urlpatterns = [
    path('', Index),
    path('users/', include('users.urls')),
]