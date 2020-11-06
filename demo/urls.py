from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

from . import views


admin.AdminSite.site_header = '留言管理系统'
admin.AdminSite.site_title = '留言管理系统V1.0.0'

 
urlpatterns = [

    path('', views.IndexView.as_view()),

    path('admin/', admin.site.urls),

    re_path(r'^api', include('api.urls')),

    re_path(r'^api-auth/', include('rest_framework.urls')),

    # 当 Debug 为 False 静态文件配置
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    re_path('^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}, name='media'),

]
