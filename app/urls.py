from django.urls import path
from app import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/', views.categoria_form, name='categoria_form'),
    path('producto/', views.producto_form, name='producto_form'),
    path('cliente/', views.cliente_form, name='cliente_form'),
    path('buscar/', views.buscar, name='buscar'),
]