from django.urls import path
from .views import haydovchi_qidirish

urlpatterns = [
    path('qidirish/', haydovchi_qidirish, name='qidirish'),
]
