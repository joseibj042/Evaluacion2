from django.urls import path
from . import views

app_name = 'inicio_benavides'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('tema/<int:tema_id>/', views.detalle_tema, name='detalle'),
]