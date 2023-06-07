from django.urls import path
from . import views

urlpatterns = [
    path ('listaV/', views.ventalist, name= "venta_list" )
]
