"""project_ims URL Configuration

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
from ims import views
from django.urls import include
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    # path('login/', views.login),
    path('ims/',views.ims),
    path('logout/', views.logout),
    path("img/", views.img),
    path("demo/", views.test_ims_app),
    path("api/", views.api),
    path("table/",views.table),

]