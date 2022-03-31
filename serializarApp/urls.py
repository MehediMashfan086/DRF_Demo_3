from django.urls import path, include
from .views import *

urlpatterns = [
    path('', post_list, name='list'),
    path('<int:pk>/', post_detail, name='post_detail'),
]