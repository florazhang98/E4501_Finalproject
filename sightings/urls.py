from django.urls import path

from .import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.list_sq, name='list_sq'),
    path('stats', views.stats, name = 'stats'),
    path('add/', views.add_sq, name = 'add_sq'),
    path('<str:squirrel_id>/', views.edit_sq, name='edit_sq'),
]
