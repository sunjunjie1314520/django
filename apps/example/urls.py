
from django.urls import path, include
from django.http import JsonResponse

from .models import User

from . import views

def Index(request):
    return JsonResponse({
        'position': 'EXAMPLE MODULE',
    })

urlpatterns = [
    path('', Index),
    path('/test', views.BookListView.as_view()),
    path('/test/<int:book_id>',views.BookDetailView.as_view())
]