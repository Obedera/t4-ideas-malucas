from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('remover_ideia/<int:id>', views.remover_ideia),
    path('sobre', views.sobre),
    path('login',views.login),
    path('ideias',views.cadastrar_ideia)
]