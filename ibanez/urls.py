from django.urls import path
from . import views

app_name = 'ibanez'

urlpatterns = [
    path('', views.view_home, name='home'),
    path('produtos/', views.view_produtos, name='produtos'),
    path('produtos/produto/<int:id>', views.view_produto, name='produto'),
]