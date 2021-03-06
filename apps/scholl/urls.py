from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('/submit', views.SubmitView.as_view()),
    path('/list', views.RecordListlView.as_view()),
    path('/list/<int:pk>', views.BookDetailView.as_view()),
    path('/recharge', views.RechargeView.as_view()),
    path('/record', views.ShowRechargeRecordView.as_view()),
    path('/config', views.AppConfigView.as_view()),
    path('/statistics', views.PanelView.as_view()),
]