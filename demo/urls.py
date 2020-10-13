from django.contrib import admin
from django.urls import path, include, re_path

admin.AdminSite.site_header = '留言管理系统'
admin.AdminSite.site_title = '留言管理系统V1.0.0'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    re_path(r'^api-auth/', include('rest_framework.urls'))
]
