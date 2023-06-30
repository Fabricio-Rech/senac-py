from django.urls import path
from . import views

app_name = 'ibanez'

urlpatterns = [
    path('', views.view_home),
    path('produto', views.view_produto),
]