
from django.urls import path, include
from django.http import JsonResponse

from . import views

def Index(request):
    return JsonResponse({
        'position': 'EXAMPLE MODULE',
    })


urlpatterns = [
    path('', Index),
    path('/test', views.BookListView.as_view()),
    path('/test/<int:pk>', views.BookDetailView.as_view()),
    path('/auth', views.AuthView.as_view()),

    path('/news_detail/<int:pk>', views.NewsDetailView.as_view()),
]