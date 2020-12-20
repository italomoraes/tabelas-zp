from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('empreendimento/<int:pk>/', views.empreendimento_detalhes, name='empreendimento_detalhes'),
    path('casa/<int:pk>/', views.casa_detalhes, name='casa_detalhes'),
]