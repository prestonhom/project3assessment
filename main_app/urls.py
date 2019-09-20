from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widget/<int:widget_id>/', views.widget_delete, name='widget_delete')
    # path('', views.pokemon_create, name='pokemon_create')
    # path('admin/', views.admin, name='admin'),
    
]
