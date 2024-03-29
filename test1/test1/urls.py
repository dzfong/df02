"""test1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

# 导入包含的包
from django.urls import include

# 项目的url文件
urlpatterns = [
    path('admin/', admin.site.urls),		#配置项目
    path('', include('booktest.urls')),				#配置应用
    path('', include('booktest.urls', namespace='news')),
    path('paper/', include('booktest.urls', namespace='paper')),
]
