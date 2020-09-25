
from django.urls import path
from django.http import JsonResponse

from .models import Person

def abc(request):
    return JsonResponse({
        'name': 'xxxxxxxxxxxxxxxxxx',
    })

def add(request):
    Person(first_name='李', last_name='子').save()
    return JsonResponse({
        'msg': '内容增加成功',
    })

urlpatterns = [
    path('', abc),
    path('add', add),
]