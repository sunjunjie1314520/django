from django.urls import path


from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/code', views.SourceCode.as_view()),
    path('/type', views.TypesAll.as_view()),
]
