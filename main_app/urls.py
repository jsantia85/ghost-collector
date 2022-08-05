from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('ghosts/', views.ghosts_index, name='ghosts_index'),
  path('ghosts/<int:ghost_id>/', views.ghosts_detail, name='ghosts_detail'),
  path('ghosts/create/', views.GhostCreate.as_view(), name='ghosts_create'),
  path('ghosts/<int:pk>/update/', views.GhostUpdate.as_view(), name='ghosts_update'),
  path('ghosts/<int:pk>/delete/', views.GhostDelete.as_view(), name='ghosts_delete'),
]