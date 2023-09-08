from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categroy/<str:slug>', get_category, name='category'),
]
