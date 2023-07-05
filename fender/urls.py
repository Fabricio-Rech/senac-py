from django.urls import path
from . import views

app_name = 'fender'

urlpatterns = [
    path('', views.view_home, name="home"),
    path('produto', views.view_produto, name="produto"),
]