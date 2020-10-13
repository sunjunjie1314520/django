from django.urls import path, include
from .views import Index, AddressViewSet

urlpatterns = [
    path('', Index),
    path('address', AddressViewSet.as_view()),
]