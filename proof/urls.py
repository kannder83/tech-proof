from django.urls import path
from . import views

urlpatterns = [
    path('', views.registers_list, name='registers_list'),
    path('register/<int:pk>/', views.register_detail, name='register_detail'),
    path('register/new', views.register_new, name='register_new'),
    path('register/<int:pk>/edit/', views.register_edit, name='register_edit'),
    path('register/<int:pk>/delete/',
         views.register_delete, name='register_delete'),
]
