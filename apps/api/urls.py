
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/users', include('users.urls')),
    path('/operation/', include('operation.urls')),
    path('/message', include('message.urls')),
    path('/barber', include('barber.urls')),
    path('/example', include('example.urls')),
    path('/applets', include('applets.urls')),
    path('/scholl', include('scholl.urls')),
    path('/upload', include('upload.urls')),
    path('/goods', include('goods.urls')),
]
