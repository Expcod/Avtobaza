"""
URL configuration for avtomobil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from mashina.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='index'),
    path('qidirish/', haydovchi_qidirish, name='haydovchi_qidirish'),
    path('get_suggestions/', get_suggestions, name='get_suggestions'),
    path('result/<int:haydovchi_id>/', result_page, name='result_page'),
]

