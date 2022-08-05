from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('ghosts/', views.ghosts_index, name='ghosts_index'),
  path('ghosts/<int:ghost_id>/', views.ghosts_detail, name='ghosts_detail'),
  path('ghosts/create/', views.GhostCreate.as_view(), name='ghosts_create'),
  path('ghosts/<int:pk>/update/', views.GhostUpdate.as_view(), name='ghosts_update'),
  path('ghosts/<int:pk>/delete/', views.GhostDelete.as_view(), name='ghosts_delete'),
  path('ghosts/<int:ghost_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
  path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
  path('toys/', views.ToyList.as_view(), name='toys_index'),
  path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
  path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
  path('ghosts/<int:ghost_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
  path('accounts/signup/', views.signup, name='signup'),
]