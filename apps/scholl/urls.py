from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/submit', views.SubmitView.as_view()),
    path('/list/<int:pk>', views.BookDetailView.as_view()),
]